import gradio as gr
from pyngrok import ngrok
from app import setup  # Your Gradio app function

# Optional: read API keys from environment
import os
os.environ.get("SERPER_API_KEY")  # example usage

# Set up public tunnel
public_url = ngrok.connect(7860)
print(f"Gradio public URL: {public_url}")

# Launch Gradio app
app = setup()  # replace with your Gradio app function
app.launch(server_name="0.0.0.0", server_port=7860)
