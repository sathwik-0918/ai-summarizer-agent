from google.adk import Agent
from google.genai import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("GOOGLE_API_KEY"))


def summarize_text(text: str) -> str:
    words = text.split()
    short = " ".join(words[:40])
    return "Summary: " + short + ("..." if len(words) > 40 else "")

root_agent = Agent(
    name="summarizer_agent",
    description="Summarizes input text using Gemini",
    tools=[summarize_text],
)