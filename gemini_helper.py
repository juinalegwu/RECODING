 
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
def suggest_solution(ticket):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key not found."

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=120000)
    )

    prompt = f"""
    You are an IT support assistant.

    Suggest simple troubleshooting steps for this ticket.

    Ticket ID: {ticket.get('id', 'Not set')}
    Title: {ticket.get('title', 'Not set')}
    Category: {ticket.get('category', 'Not set')}
    Urgency: {ticket.get('urgency', 'Not set')}
    Priority: {ticket.get('priority', 'Not set')}

    Give 3 practical troubleshooting steps.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=600,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        return response.text if response.text else "Gemini returned no suggestions."
    except Exception as error:
        return f"Could not get suggestions from Gemini: {error}"
