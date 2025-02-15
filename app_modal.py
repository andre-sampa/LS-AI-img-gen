# gradio_interface.py
import gradio as gr
import modal
from config.models import models_modal  # Indirect import
#from img_gen import generate_image

print("Hello from gradio_interface_head!")

# Modal remote function synchronously
def generate(adventurer_id,
            #prompt_dropdown,
            #character_dropdown,
            scene_dropdown,
            #model_dropdown, 
            custom_prompt_input,
            cpu_gpu ="GPU",
        ):
    # Debug: 
    debug_message = f"Debug: Button clicked! Inputs - ID: {adventurer_id}, Scene: {scene_dropdown}, Custom Prompt: {custom_prompt_input}"
    print(debug_message)  # Print to console for debugging
    try:
        # Check for CPU/GPU dropdown option
        if cpu_gpu == "GPU":
            f = modal.Function.from_name("LS-img-gen-modal", "generate_image_gpu")
        else:
            f = modal.Function.from_name("LS-img-gen-modal", "generate_image_cpu")

        print ("Sending to external function")
       # Import the remote function
        image_path, message = f.remote(
                            adventurer_id,
                            #prompt_dropdown, 
                            #character_dropdown,
                            scene_dropdown,
                            #model_dropdown,
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
        gr.Markdown("# ========== Loot Survivor - AI Image Generator ========== modal GPU")
        with gr.Row():
            # Set default values for dropdowns
            #prompt_dropdown = gr.Dropdown(choices=[p["alias"] for p in prompts], label="Select Beast", value=prompts[0]["alias"])
            adventurer_id = gr.Number(label="Adventurer ID:")
            #character_dropdown = gr.Dropdown(choices=["Wizard", "Hunter", "Warrior"], label="Select Character Type", value="Wizard")
            scene_dropdown1 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Adventurer Portait", visible=False )          
            scene_dropdown2 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Beast Portait", visible=False )          
            scene_dropdown3 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Encounter", visible=False )          
            scene_dropdown4 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Last Battle", visible=False )          
            scene_dropdown5 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Loot Bag", visible=False )          
            custom_prompt_input = gr.Textbox(label="Custom Prompt (Optional)", placeholder="Enter additional details (max 200 chars)...", max_lines=1, max_length=200)
            #model_dropdown = gr.Dropdown(choices=[m["alias"] for m in models], label="Select Model", value=models[0]["alias"])
        #with gr.Row():
            # Add a text box for custom user input (max 200 characters)
        with gr.Row():
            generate_button = gr.Button("Generate Image")
        with gr.Row():
            output_image1 = gr.Image(elem_classes="output-image", label="Adventurer Portait", show_label=True, scale=1, width="100%")
            output_image2 = gr.Image(elem_classes="output-image", label="Beast Portait", show_label=True, scale=1, width="100%")
        with gr.Row():
            output_image3 = gr.Image(elem_classes="output-image", label="Encounter", show_label=True, scale=1, width="100%")
            output_image4 = gr.Image(elem_classes="output-image", label="Last Battle", show_label=True, scale=1, width="100%")
            output_image5 = gr.Image(elem_classes="output-image", label="Loot Bag", show_label=True, scale=1, width="100%")
        
        with gr.Row():
            status_text = gr.Textbox(label="Status", placeholder="Waiting for input...", interactive=False)
        # Connect the button to the function
        generate_button.click(
            generate,
            inputs=[adventurer_id,
                    #prompt_dropdown, 
                    #character_dropdown,
                    scene_dropdown1,
                    #model_dropdown,
                    custom_prompt_input,
                    ],
            outputs=[output_image1, status_text],
            show_progress_on=output_image1,
        )
        generate_button.click(
            generate,
            inputs=[adventurer_id,
                    #prompt_dropdown, 
                    #character_dropdown,
                    scene_dropdown2,
                    #model_dropdown,
                    custom_prompt_input,
                    ],
            outputs=[output_image2, status_text],
            show_progress_on=output_image2,

        )
        generate_button.click(
            generate,
            inputs=[adventurer_id,
                    #prompt_dropdown, 
                    #character_dropdown,
                    scene_dropdown3,
                    #model_dropdown,
                    custom_prompt_input,
                    ],
            outputs=[output_image3, status_text],
            show_progress_on=output_image3,

        )
        generate_button.click(
            generate,
            inputs=[adventurer_id,
                    #prompt_dropdown, 
                    #character_dropdown,
                    scene_dropdown4,
                    #model_dropdown,
                    custom_prompt_input,
                    ],
            outputs=[output_image4, status_text],
            show_progress_on=output_image4,

        )        
        generate_button.click(
            generate,
            inputs=[adventurer_id,
                    #prompt_dropdown, 
                    #character_dropdown,
                    scene_dropdown5,
                    #model_dropdown,
                    custom_prompt_input,
                    ],
            outputs=[output_image5, status_text],
            show_progress_on=output_image5,

        )
        
    return demo

# Create the demo instance
demo = gradio_interface()

# Only launch if running directly
if __name__ == "__main__":
        demo.queue().launch()