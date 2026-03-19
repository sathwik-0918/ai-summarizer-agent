from google.adk import Agent
from google.genai import Client

client = Client()

def summarize_text(text: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"Summarize this text:\n{text}"
    )
    return response.text

root_agent = Agent(
    name="summarizer_agent",
    description="Summarizes input text using Gemini",
    tools=[summarize_text],
)