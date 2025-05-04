import google.generativeai as genai
from utils.api_config import api_config

# --- Configuration ---
api_config()

# Choose the model
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Start a chat session
chat = model.start_chat(history=[])  # Start with an empty history

print("Starting chat with Gemini. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Ending chat.")
        break

    try:
        print("\nGemini thinking...")
        # Send the user's message to the chat
        response = chat.send_message(user_input)

        # Print Gemini's reply
        print(f"\nGemini: {response.text}\n")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        # You might want to break the loop here or allow the user to retry
