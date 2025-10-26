import asyncio
from pyngrok import ngrok
from app import setup  # your async setup function

# Open public ngrok tunnel
public_url = ngrok.connect(7860)
print(f"Gradio public URL: {public_url}")

# Run your async setup function and launch Gradio
async def main():
    app = await setup()  # your setup() should return a Gradio Blocks object
    app.launch(server_name="0.0.0.0", server_port=7860)

asyncio.run(main())
