import gradio as gr
from PIL import Image
import os

def create_gif(files, duration):
    frames = []

    # SORT images
    image_files = sorted(files)

    # First image
    first_image = Image.open(image_files[0]).convert("RGB")
    size = first_image.size
    frames.append(first_image)

    # Process rest
    for file in image_files[1:]:
        img = Image.open(file).convert("RGB")
        img = img.resize(size)
        frames.append(img)

    gif_path = "output.gif"

    # SAVE GIF (slower)
    frames[0].save(
        gif_path,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=int(duration * 1000),
        loop=0
    )

    # 👉 Return for preview + download
    return gif_path, gif_path


# UI
interface = gr.Interface(
    fn=create_gif,
    inputs=[
        gr.File(file_count="multiple", type="filepath", label="Upload Images"),
        gr.Slider(0.1, 2, value=0.5, label="Frame Duration (seconds)")
    ],
    outputs=[
        gr.Image(label="Preview GIF"),   # 👈 show on screen
        gr.File(label="Download GIF")    # 👈 download
    ],
    title="GIF Creator",
    description="Upload images in sequence to create a GIF"
)

interface.launch()