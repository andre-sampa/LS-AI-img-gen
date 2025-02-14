# Import gradio_interface
import os
from app_modal import demo
# Debug: Print environment variables
print("MODAL_TOKEN_ID:", os.getenv("MODAL_TOKEN_ID"))
print("MODAL_TOKEN_SECRET:", os.getenv("MODAL_TOKEN_SECRET"))

port = int(os.environ.get("PORT", 7860))  # Use Render's PORT or default to 7860
token_id = os.getenv("MODAL_TOKEN_ID")
token_secret = os.getenv("MODAL_TOKEN_SECRET")
# Launch the Gradio app
demo.launch(server_name="0.0.0.0", server_port=port)