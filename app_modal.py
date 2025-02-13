# gradio_interface.py
import gradio as gr
import modal
from config.config import prompts, models_modal  # Indirect import
#from img_gen import generate_image

print("Hello from gradio_interface_head!")

# Modal remote function synchronously
def generate(prompt_dropdown, team_dropdown, model_dropdown, custom_prompt_input, cpu_gpu ="GPU"):
    # Debug: 
    debug_message = f"Debug: Button clicked! Inputs - Prompt: {prompt_dropdown}, Team: {team_dropdown}, Model: {model_dropdown}, Custom Prompt: {custom_prompt_input}"
    print(debug_message)  # Print to console for debugging
    try:
        # Check for CPU/GPU dropdown option
        if cpu_gpu == "GPU":
            f = modal.Function.from_name("LS-img-gen-modal", "generate_image_gpu")
        else:
            f = modal.Function.from_name("LS-img-gen-modal", "generate_image_cpu")

       # Import the remote function
        image_path, message = f.remote(
                            prompt_dropdown, 
                            team_dropdown, 
                            model_dropdown, 
                            custom_prompt_input,
                            )
        return image_path, message
    except Exception as e:
        return None, f"Error calling generate_image function: {e}"
    

# Gradio Interface
def gradio_interface():
    with gr.Blocks(css="""
                    .gradio-container {
                        background-image: url(''); 
                        background-size: cover;
                        background-position: center;
                    }
                    .output-image img {
                     width: 2500px; /* Force image to fill container width */
                     object-fit: cover; /* ACTIVATE FOR IMAGE-FIT CONTAINER */
                    }
                    """) as demo:
        gr.Markdown("# ========== Loot Survivor - AI Image Generator ==========")
        with gr.Row():
            # Set default values for dropdowns
            prompt_dropdown = gr.Dropdown(choices=[p["alias"] for p in prompts], label="Select Beast", value=prompts[0]["alias"])
            character_dropdown = gr.Dropdown(choices=["Beast only", "Wizard", "Warrior"], label="Select Character", value="Beast only")
            model_dropdown = gr.Dropdown(choices=[m["alias"] for m in models_modal], label="Select Model", value=models_modal[0]["alias"])
        with gr.Row():
            # Add a text box for custom user input (max 200 characters)
            custom_prompt_input = gr.Textbox(label="Custom Prompt (Optional)", placeholder="Enter additional details (max 200 chars)...", max_lines=1, max_length=200)
        with gr.Row():
            generate_button = gr.Button("Generate Image")
        with gr.Row():
            output_image = gr.Image(elem_classes="output-image", label="Generated Image", show_label=False, scale=1, width="100%")
        with gr.Row():
            status_text = gr.Textbox(label="Status", placeholder="Waiting for input...", interactive=False)


        # Import the remote function
        f = modal.Function.from_name("img-gen-modal-gpu", "generate_image")
        
        # Connect the button to the function
        generate_button.click(
            generate,
            inputs=[prompt_dropdown, 
                    custom_prompt_input,
                    character_dropdown,
                    model_dropdown
                    ],
            outputs=[output_image, status_text]
        )
    return demo

# Create the demo instance
demo = gradio_interface()

# Only launch if running directly
if __name__ == "__main__":
        demo.queue().launch()