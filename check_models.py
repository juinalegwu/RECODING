import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found.")
else:
    try:
        client = genai.Client(api_key=api_key)

        for model in client.models.list():
            name = model.name or ""

            if "flash" in name.lower():
                print(name)

    except Exception as error:
        print("Could not list models:")
        print(error)
 