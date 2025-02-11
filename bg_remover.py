from PIL import Image
import numpy as np
from rembg import remove

def remove_background(input_image_path, output_image_path):
    """
    Removes the background from an image and saves the result.

    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the output image with background removed.

    Returns:
        None
    """
    try:
        # Open the input image
        with open(input_image_path, 'rb') as img_file:
            input_image = img_file.read()

        # Remove the background
        output_image = remove(input_image)

        # Save the resulting image
        with open(output_image_path, 'wb') as out_file:
            out_file.write(output_image)

        print(f"Background removed and saved to {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Provide the paths to your input and output images
input_image_path = r"C:\Users\user\Downloads\DALL·E 2025-01-21 10.09.12 - A clean and modern favicon design inspired by the logo 'TradeIQ', focusing on the combination of blue and orange colors. The design should emphasize s.webp"
output_image_path = "output_image.png"
remove_background(input_image_path, output_image_path)
