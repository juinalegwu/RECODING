import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env", override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


def ask_ai(question):
    """Send a question to Google's AI and return its answer."""
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question
        )
        return response.text

    except Exception as error:
        print("Error details:", error)
        return "Sorry, the AI service is unavailable. Please try again."


if __name__ == "__main__":
    answer = ask_ai("Explain a Python list to a beginner in three sentences.")
    print(answer)
