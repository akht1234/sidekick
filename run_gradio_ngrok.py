import os
import gradio as gr
from pyngrok import ngrok
from app import setup  # your Gradio app setup function

# Example: reading API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

# Optionally, pass keys to your classes/functions if needed
# e.g., serper = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

# Start ngrok public tunnel
public_url = ngrok.connect(7860)
print(f"Gradio public URL: {public_url}")

# Launch the Gradio app
app = setup()  # your Gradio app function
app.launch(server_name="0.0.0.0", server_port=7860)
