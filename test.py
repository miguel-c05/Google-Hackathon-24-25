from PIL import Image, ImageDraw
import json

def draw_path_on_image(image_path, json_path, output_path="path_drawn_image.png"):
    """
    Draws a path on an image based on coordinates from a JSON file.

    Args:
        image_path: Path to the image file.
        json_path: Path to the JSON file containing the path coordinates.
        output_path: Path to save the image with the path drawn.
    """

    try:
        # Load the image
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        # Load the coordinates from the JSON file
        with open(json_path, 'r') as f:
            data = json.load(f)
            path_coordinates = data['path']

        # Draw the path
        for i in range(len(path_coordinates) - 1):
            x1 = path_coordinates[i]['x']
            y1 = path_coordinates[i]['y']
            x2 = path_coordinates[i+1]['x']
            y2 = path_coordinates[i+1]['y']
            draw.line((x1, y1, x2, y2), fill="blue", width=3)  # You can adjust the color and width

        # Save the modified image
        img.save(output_path)
        print(f"Path drawn and saved to {output_path}")

    except FileNotFoundError:
        print("Error: Image or JSON file not found.")
    except KeyError:
        print("Error: 'path' key not found in JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage (replace with your actual file paths)
image_file = "FC6_0.png"  # Replace with the actual path to your image file
json_file = "coords.json" # Replace with the actual path to your json file (containing the JSON I provided previously)
output_file = "path_drawn_image.png"  # Optional: Specify a different output file name

draw_path_on_image(image_file, json_file, output_file)