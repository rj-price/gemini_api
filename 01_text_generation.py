import google.generativeai as genai
from utils.api_config import api_config

# Configure the API key
api_config()

# Choose the model
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# The text prompt you want to send to the model
prompt = "Write a four-line poem about a curious puppy exploring a garden."

try:
    # Send the prompt to the model
    print("\nSending prompt to Gemini...")
    response = model.generate_content(prompt)

    # Print the response text
    print("\nGemini's Response:")
    # Basic error check for the response object
    if response and hasattr(response, "text"):
        print(response.text)
    else:
        print("Received an unexpected response format.")
        # You might want to print the whole response object for debugging:
        # print(response)

except Exception as e:
    print(f"\nAn error occurred during generation: {e}")
