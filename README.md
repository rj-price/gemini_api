# Beginner's Guide to Gemini API

Let's dive into the world of Google's Gemini API using Python! This guide will take you from zero to generating text with Gemini, complete with examples and practice projects.

### What is the Gemini API?

Think of the Gemini API as a way for your Python programs to talk to Google's powerful AI models (like Gemini Pro). You can ask it to write stories, answer questions, summarize text, translate languages, write code, and much more, all by sending it simple text prompts.

### Why Use Python?

Python is a fantastic language for beginners and widely used in AI and data science. Google provides an official Python library (`google-generativeai`) that makes interacting with the Gemini API straightforward.



## Setting Up Your Environment

Before you can write any code, you need two things:

1.  **Python:** You need Python installed on your computer. Most modern operating systems (macOS, Linux) have it pre-installed. Windows users might need to install it from [python.org](https://www.python.org/).
    * *How to check:* Open your terminal or command prompt and type `python --version` or `python3 --version`. You should see a version number (ideally 3.7 or higher).
2.  **A Google API Key:** This is like a password that allows your code to access the Gemini API. It proves that *you* are making the request.
    * *How to get one:*
        * Go to [Google AI Studio](https://aistudio.google.com/).
        * You'll likely need to sign in with your Google account.
        * Look for an option like "Get API key" or navigate to the API key section.
        * Create a new API key.
        * **VERY IMPORTANT:** Copy this key and save it somewhere secure. Treat it like a password – don't share it publicly or commit it directly into your code repository (like GitHub).



## Installation and Basic Configuration

1.  **Install the Library:** Open your terminal or command prompt and install the official Google library using pip (Python's package installer):
    ```bash
    pip install google-generativeai
    ```

2.  **Configure Your API Key (Securely):**
    The best practice is *not* to put your API key directly in your script. Instead, copy or rename `.example.env` to `.env` and put your API key inside it. Install `python-dotenv` (`pip install python-dotenv`), so that you can access this key by using the `api_config.py` utility:

    ```python
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


    ```



## Example 1: Your First Text Generation

Let's ask Gemini to do something simple, like write a short poem.

```python
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

```

**Explanation:**

1.  `import google.generativeai as genai`: Imports the library.
2. `from utils.api_config import api_config`: Imports the API configuration utility.
3.  `api_config()`: Sets up your authentication using the key loaded from the `.env` file.
4.  `model = genai.GenerativeModel('gemini-2.0-flash-lite')`: Creates an instance of the model you want to use. `gemini-2.0-flash-lite` is a good for quick text generation.
5.  `prompt = "..."`: Defines the instruction you're giving the AI.
6.  `response = model.generate_content(prompt)`: This is the core command! It sends your `prompt` to the Gemini model and waits for a `response`.
7.  `print(response.text)`: The generated text is usually found in the `.text` attribute of the `response` object.

**Run this script**: You should see your API key confirmation message, the "Sending prompt..." message, and then Gemini's poetic output.

**Tip**: Experiment with changing the model and prompt, and see how the responses change. 

---

## Example 2: Having a Conversation (Chat)

Gemini can also remember the context of a conversation. Let's build a simple chat bot.

```python
import google.generativeai as genai
from utils.api_config import api_config

# Configure the API key
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

```

**Explanation:**

1.  `chat = model.start_chat(history=[])`: Instead of `generate_content`, we use `start_chat()`. This creates a chat object that keeps track of the conversation history.
2.  `while True:`: Creates a loop so you can keep talking.
3.  `user_input = input("You: ")`: Gets your message from the terminal.
4.  `if user_input.lower() == 'quit':`: Allows you to exit the loop.
5.  `response = chat.send_message(user_input)`: Sends your message *within the context of the ongoing chat*. Gemini will consider previous messages when generating its response.
6.  `print(f"\nGemini: {response.text}\n")`: Prints the reply.

**Run this script**: You should see your API key confirmation message, the "Starting chat with Gemini..." message, and then a "You:" prompt where you can enter a question.

**Tip**: Try asking a question, then asking a follow-up question that refers back to the previous answer (e.g., "What is the capital of France?", followed by "What is the population of that city?"). Gemini should understand the context.



## Practice Projects

Now it's your turn! Try building these small projects.

### Project 1: Simple Content Generator

* **Goal:** Get comfortable with `generate_content`.
* **Task:** Write a script that asks the user what kind of content they want (e.g., "a joke", "a short story", "an explanation of black holes") and then generates it using `generate_content`.
* **Challenge:** Can you make the script ask for a *topic* as well? (e.g., "Tell me a joke about *computers*").

### Project 2: Basic "Remember Me" Bot

* **Goal:** Understand chat history.
* **Task:** Using the chat example (`start_chat`), modify it so the *first* message you send tells the bot your name. In subsequent messages, ask it "What is my name?". See if it remembers.
* **Challenge:** Can you make the initial "memory" message a bit more complex, like storing your name *and* favorite color? Then ask about both later.

### Project 3: Text Summarizer

* **Goal:** Apply Gemini to a practical task.
* **Task:** Write a script that:
    1.  Takes a long piece of text as input (you can paste it in or read it from a file).
    2.  Creates a prompt like: "Summarize the following text in three sentences: [Your long text here]".
    3.  Uses `generate_content` to get the summary.
    4.  Prints the summary.
* **Challenge:** Add error handling. What if the text is too long for the API? (Check the Gemini documentation for input limits). What if the response doesn't contain text?

### Project 4: Simple Command Bot

* **Goal:** Combine chat with structured prompts.
* **Task:** Create a chat bot where you can give it simple commands like:
    * `translate: [text] to [language]` (e.g., `translate: Hello world to Spanish`)
    * `explain: [topic]` (e.g., `explain: quantum physics simply`)
    * `write: a [genre] story about [topic]` (e.g., `write: a sci-fi story about a lost robot`)
    * Your script needs to parse the user's input, figure out the command, construct the *actual* prompt to send to Gemini, and then display the result. Use the `chat.send_message()` method.
* **Challenge:** How would you handle commands it doesn't recognize? Can you make the "write" command ask for more details (like characters or setting) in follow-up messages?



## Next Steps and Important Considerations

1.  **Explore the Documentation:** The official [Google AI Python SDK documentation](https://www.google.com/search?q=https://ai.google.dev/docs/python_sdk) is your best friend. It covers more advanced features like:
    * **Safety Settings:** Controlling potentially harmful content generation.
    * **Generation Configuration:** Adjusting `temperature` (randomness) and `top_k`/`top_p` (sampling strategy).
    * **Function Calling:** Making the model call external tools or APIs (more advanced).
    * **Embedding:** Representing text as numerical vectors (useful for search, clustering).
    * **Vision Models:** Analyzing images (e.g., using `gemini-pro-vision`).
2.  **Error Handling:** Real-world applications need robust error handling. What happens if the API is down? If your key is invalid? If you hit rate limits? Use `try...except` blocks generously.
3.  **API Key Security:** Reiterate: **Never** commit your API key to version control (like Git/GitHub). Use environment variables or a secrets management system.
4.  **Costs:** While there's often a free tier to get started, using the API (especially heavily) can incur costs. Check the [Google AI pricing page](https://ai.google.dev/pricing) for details.
5.  **Rate Limits:** Be aware of how many requests you can make per minute. The documentation or error messages will provide information on this.

---

You've now got the basics of using the Gemini API with Python! The key is to experiment, read the documentation, and start building. Good luck, and have fun exploring the possibilities!

# Acknowledgements
This guide was written in collaboration with Gemini 2.5 Pro.