import os, time
import gradio as gr
from pyngrok import ngrok
from app import setup

# Start tunnel
public_url = ngrok.connect(7860)
print(f"\n🌍 Your Gradio App is live at: {public_url.public_url}\n", flush=True)

# Launch in background thread
app = setup()
app.launch(server_name="0.0.0.0", server_port=7860, share=False, prevent_thread_lock=True)

# Keep alive for 30 minutes (adjust as needed)
print("App is running... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(600)
except KeyboardInterrupt:
    print("Shutting down app...")

