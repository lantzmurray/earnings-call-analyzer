"""
Backend API for Earnings Call Summarizer using Mistral via Ollama.

This FastAPI application processes earnings call transcripts and extracts
key financial metrics, strategic initiatives, management guidance, and
market sentiment to provide comprehensive investment-relevant summaries.
"""

from fastapi import FastAPI, Form
import requests
import json

app = FastAPI()
OLLAMA_TIMEOUT_SECONDS = 1800

OLLAMA_API_URL = "http://localhost:11434/api/generate"


def read_ollama_stream(response: requests.Response) -> str:
    """Read Ollama's streamed NDJSON chunks into one response string."""
    chunks = []
    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue
        data = json.loads(line)
        chunks.append(data.get("response", ""))
        if data.get("done"):
            break
    return "".join(chunks).strip()


def call_ollama(payload: dict) -> str:
    """Call Ollama with streaming enabled so long local generations stay alive."""
    streamed_payload = {**payload, "stream": True}
    with requests.post(
        OLLAMA_API_URL,
        json=streamed_payload,
        timeout=(10, OLLAMA_TIMEOUT_SECONDS),
        stream=True,
    ) as response:
        response.raise_for_status()
        return read_ollama_stream(response)

@app.post("/summarize/")
def summarize_earnings(text: str = Form(...)):
    """
    Generate a comprehensive earnings call summary.

    Uses Mistral to analyze earnings call transcripts and extract:
    - Key financial metrics and performance highlights
    - Strategic initiatives and future guidance
    - Management tone and market sentiment
    - Notable Q&A insights

    Args:
        text: Earnings call transcript text (from HTML form data)

    Returns:
        A dictionary containing the earnings summary
    """
    # Construct a comprehensive prompt for earnings analysis
    # Request structured output including executive summary, metrics, sentiment, and implications
    # This helps investors quickly understand the key investment-relevant information
    prompt = (
        "Analyze this earnings call transcript and provide:\n\n"
        "1. EXECUTIVE SUMMARY: 2-3 sentence overview of the call\n"
        "2. KEY FINANCIAL METRICS: Revenue, profit, guidance highlights\n"
        "3. STRATEGIC INITIATIVES: New projects, investments, partnerships\n"
        "4. MANAGEMENT SENTIMENT: Optimistic, cautious, confident?\n"
        "5. NOTABLE Q&A INSIGHTS: Important questions and responses\n"
        "6. INVESTMENT IMPLICATIONS: What this means for investors\n\n"
        f"Transcript:\n{text}"
    )

    # Send the transcript to Ollama using Mistral for financial analysis.
    # The helper streams chunks from Ollama, then returns one complete summary.
    result = call_ollama({
        "model": "mistral",  # Mistral for financial analysis
        "prompt": prompt,     # Structured prompt for comprehensive earnings analysis
    })

    # Return the earnings summary to the frontend.
    return {"summary": result}
