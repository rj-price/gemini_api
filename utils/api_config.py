import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


def api_config():
    """
    This function loads the API key from an environment variable and sets it for the Google Generative AI client.
    """
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "API key not found. Set the GOOGLE_API_KEY environment variable."
            )
        genai.configure(api_key=api_key)
        print("API Key configured.")
    except ValueError as e:
        print(e)
        exit()
    except Exception as e:
        print(f"An unexpected error during configuration: {e}")
        exit()
