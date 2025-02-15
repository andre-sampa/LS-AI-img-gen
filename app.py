# app.py 
# venv w python3.11 
from config.config import api_token  # Direct import
from config.models import models
import gradio as gr
from src.img_gen import generate_image
from metadata.metadata import fetch_metadata
import time

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
            #prompt_dropdown = gr.Dropdown(choices=[p["alias"] for p in prompts], label="Select Beast", value=prompts[0]["alias"])
            adventurer_id = gr.Number(label="Adventurer ID:")
            #character_dropdown = gr.Dropdown(choices=["Wizard", "Hunter", "Warrior"], label="Select Character Type", value="Wizard")
            scene_dropdown1 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Adventurer Portait", visible=False )          
            scene_dropdown2 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Beast Portait", visible=False )          
            scene_dropdown3 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Encounter", visible=False )          
            scene_dropdown4 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Loot Bag"], label="Select Scene", value="Last Battle", visible=False )          
            scene_dropdown5 = gr.Dropdown(choices=["Adventurer Portait", "Encounter", "Beast Portait", "Last Battle", "Final Scene"], label="Select Scene", value="Final Scene", visible=False )          
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
            output_image5 = gr.Image(elem_classes="output-image", label="Final Scene", show_label=True, scale=1, width="100%")
        
        with gr.Row():
            status_text = gr.Textbox(label="Status", placeholder="Waiting for input...", interactive=False)
        # Connect the button to the function
        generate_button.click(
            generate_image,
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
            generate_image,
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
            generate_image,
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
            generate_image,
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
            generate_image,
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