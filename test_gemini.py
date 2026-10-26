import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found.")
else:
    print("API key found. Connecting...")

    try:
        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=60000)
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents="Say hello in one short sentence.",
            config=types.GenerateContentConfig(
                max_output_tokens=50,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        print("Gemini replied:")
        print(response.text)

    except Exception as error:
        print("Gemini request failed.")
        print(error)

