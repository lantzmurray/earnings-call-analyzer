# Project 9: Earnings Call Analyzer (Mistral + Ollama)

An AI-powered tool for summarizing earnings call transcripts, classifying sentiment, and extracting key financial insights. Perfect for investors, analysts, and financial professionals.

## Features

- **3-Sentence Summary**: Concise overview of earnings call content
- **Sentiment Classification**: Identifies positive, neutral, or negative sentiment
- **Key Financial Insights**: Extracts growth signals, risks, and guidance
- **FastAPI Backend**: Efficient REST API for processing
- **Streamlit Frontend**: User-friendly interface for analysis
- **Local Processing**: All analysis runs locally using Ollama LLMs - no external API dependencies

## Architecture

### Backend Components

1. **Earnings Summarizer** (`backend/main.py`)
   - Processes earnings call transcripts
   - Generates comprehensive summaries
   - Extracts key financial metrics

2. **Sentiment Analyzer** (`backend/main.py`)
   - Classifies overall sentiment
   - Identifies positive/negative indicators
   - Provides sentiment context

3. **Financial Insights Extractor** (`backend/main.py`)
   - Revenue trends and growth signals
   - Forward guidance and outlook
   - Risk warnings and concerns

### Frontend Components

1. **Streamlit UI** (`frontend/app.py`)
   - User interface for transcript input
   - Results display and visualization
   - Export functionality

2. **Reusable Components** (`frontend/components.py`)
   - Modular UI elements
   - Consistent styling and layout

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running (for local LLM inference)

### Setup Steps

1. **Navigate to the project directory**:
   ```bash
   cd SchoolOfAI/Official/soai-09-earnings-call
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and start Ollama** (if not already installed):
   ```bash
   # Install Ollama from https://ollama.com
   # Pull a model (mistral is recommended)
   ollama pull mistral
   # Start Ollama service
   ollama serve
   ```

## Running the Application

### Backend API

1. **Start the FastAPI backend**:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. **Access the API**: Navigate to `http://localhost:8000` for API documentation

### Frontend UI

1. **Start the Streamlit application** (in a new terminal):
   ```bash
   streamlit run frontend/app.py
   ```

2. **Open your browser**: Navigate to `http://localhost:8501`

## Usage

### 1. Upload Earnings Transcript

- Paste the earnings call transcript in the text area
- Or upload a .txt file containing the transcript
- Sample data provided in `data/tesla_q4_2024.txt`

### 2. Analyze Earnings Call

- Click "Analyze" to process the transcript
- Wait for the AI to generate insights
- View the comprehensive results

### 3. Review Results

- **Summary**: One-paragraph overview of the call
- **Sentiment**: Overall sentiment classification
- **Key Insights**: Revenue trends, growth, guidance, risks

### 4. Export Results

- Copy the summary for reports
- Export insights as text or JSON
- Save for future reference

## Workflow

```
Upload Transcript → Backend API → Ollama LLM → Generate Analysis → Display Results
     ↓                  ↓            ↓                ↓                  ↓
  Paste text        FastAPI      Call model      Extract metrics    Show to
  or file           endpoint     with prompt     & sentiment       user
```

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
OLLAMA_MODEL=mistral
OLLAMA_API_URL=http://localhost:11434/api/generate
```

### Ollama Models

The system supports any Ollama model. Recommended models:
- `mistral` - Lightweight and efficient for financial summarization (default)
- `llama2` - Better reasoning for complex analysis

## Project Structure

```
soai-09-earnings-call/
├── backend/
│   └── main.py                  # FastAPI backend
├── frontend/
│   ├── app.py                    # Streamlit UI
│   └── components.py             # Reusable UI components
├── data/
│   └── tesla_q4_2024.txt        # Sample earnings call transcript
├── requirements.txt              # Python dependencies
└── README.md                   # This file
```

## Dependencies

- `fastapi` - Web API framework
- `uvicorn` - ASGI server
- `streamlit` - Web UI framework
- `requests` - HTTP client for Ollama API
- `python-dateutil` - Date/time parsing

## Troubleshooting

### Ollama Connection Issues

If you see connection errors:
1. Verify Ollama is running: `ollama list`
2. Check the API URL: `curl http://localhost:11434/api/generate`
3. Ensure the model is pulled: `ollama pull mistral`

### Backend API Issues

If the backend isn't responding:
1. Verify uvicorn is running: `ps aux | grep uvicorn`
2. Check the port isn't in use: `lsof -i :8000`
3. Review backend logs for errors

### Frontend Connection Issues

If the frontend can't connect to the backend:
1. Verify both services are running
2. Check the API URL in frontend/app.py
3. Ensure CORS is configured correctly

### Analysis Issues

If financial insights aren't being extracted:
1. Check that the transcript is complete and well-formatted
2. Verify the LLM model is appropriate for financial analysis
3. Review the prompt in backend/main.py
4. Try with a different model (llama2 vs mistral)

### Slow Performance

For faster analysis:
1. Use mistral for speed
2. Reduce transcript length if possible
3. Increase Ollama's GPU resources if available

## Use Cases

- **Investment Analysis**: Quick review of earnings calls for investment decisions
- **Financial Research**: Extract key metrics and guidance
- **Sentiment Tracking**: Monitor market sentiment over time
- **Report Generation**: Create summaries for presentations
- **Risk Assessment**: Identify potential risks and concerns

## Input Format

The system accepts:
- **Raw Earnings Call Transcripts**: Copy/paste or .txt files
- **Sample Data**: Provided in `data/tesla_q4_2024.txt`
- **Any Length**: Short updates to full call transcripts

## Output Format

The system generates:
- **One-Paragraph Summary**: Concise overview of the earnings call
- **Sentiment Classification**: Positive / Neutral / Negative
- **Key Financial Insights**: Including revenue trends, growth signals, forward guidance, and risk warnings

## Important Notes

- All processing happens locally - no data is sent to external servers
- Analysis quality depends on the completeness of the transcript
- Sentiment classification is AI-based and should be verified
- Financial insights are AI-generated and should be reviewed for accuracy
- Mistral is optimized for financial summarization tasks

## License

This project is part of the School of AI curriculum.
