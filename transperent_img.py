import cv2
import numpy as np

def add_alpha_channel(image):
    # Create a new image with an alpha channel (fully opaque)
    return cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

def white_to_transparent(image_path, output_path):
    # Load the image (without an alpha channel)
    image = cv2.imread(image_path)

    # Check if the image has an alpha channel, if not, add one
    if image.shape[2] == 3:  # No alpha channel (3 channels for RGB)
        image = add_alpha_channel(image)

    # Define the lower and upper bounds for white color
    lower_white = np.array([235, 235, 235, 0])  # Lower bound for white color with alpha channel set to 0
    upper_white = np.array([255, 255, 255, 255])  # Upper bound for white color with alpha channel set to 255

    # Create a binary mask where non-fully-transparent white pixels will be True (255) and the rest False (0)
    mask = cv2.inRange(image, lower_white, upper_white)

    # Set the non-fully-transparent white pixels to be fully transparent
    image[mask != 0] = [0, 0, 0, 0]

    # Save the resulting image with transparency
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    input_image_path = 'input.png'  # Replace 'input.png' with your input image file path
    output_image_path = 'output.png'  # Output file path for the transparent image
    white_to_transparent(input_image_path, output_image_path)
