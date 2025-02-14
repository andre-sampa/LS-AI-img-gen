# Import gradio_interface
import os
from app_modal import demo
port = int(os.environ.get("PORT", 7860))  # Use Render's PORT or default to 7860
# Launch the Gradio app
demo.launch(server_name="0.0.0.0", server_port=port)