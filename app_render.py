# Import gradio_interface
import os
from app_modal import demo
# Debug: Print environment variables
token_id = os.getenv("MODAL_TOKEN_ID")
token_secret = os.getenv("MODAL_TOKEN_SECRET")

print(f"MODAL_TOKEN_ID: {token_id}")
print(f"MODAL_TOKEN_SECRET: {token_secret}")

port = int(os.environ.get("PORT", 7860))  # Use Render's PORT or default to 7860
# Launch the Gradio app
demo.launch(server_name="0.0.0.0", server_port=port)