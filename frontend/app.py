"""
Frontend Application for Earnings Call Summarizer.

This Streamlit app enables financial analysts and investors to quickly
understand the key points from earnings call transcripts without
reading through lengthy documents.
"""

import os
import sys

import streamlit as st
import requests

PACKAGE_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from components import render_app_footer, run_with_status_updates

# Set the main title of the Streamlit app
st.title("Earnings Call Summarizer (Mistral)")

# Create a text area for pasting earnings call transcript
# height=400 provides ample space for lengthy transcripts
transcript = st.text_area("Paste earnings call transcript:", height=400)

# Check if the user clicked the "Generate Summary" button
if st.button("Generate Summary"):
    # Verify that a transcript has been entered
    if transcript:
        # Send the transcript to the backend API for summarization
        response = run_with_status_updates(
            lambda: requests.post(
                "http://localhost:8000/summarize/",
                data={"text": transcript}
            ),
            start_message="Summarizing the earnings call..."
        )

        # Check if the request was successful (HTTP 200)
        if response.status_code == 200:
            # Extract the summary from the JSON response
            summary = response.json().get("summary", "Error")

            # Display the earnings summary section header
            st.subheader("Earnings Summary:")

            # Render the summary on the page
            st.write(summary)
        else:
            # Display an error message if the backend request failed
            st.error("Error generating summary. Make sure the backend is running.")
    else:
        # Display a warning if no transcript was provided
        st.warning("Please paste a transcript first.")


render_app_footer()
