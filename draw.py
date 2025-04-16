from PIL import Image, ImageDraw
import json

def parse_coordinates_file(file_path):
    """
    Parse the coordinates TXT file to extract node names and their coordinates.

    Args:
        file_path: Path to the coordinates TXT file.

    Returns:
        A dictionary mapping node names to their coordinates (x, y).
    """
    nodes = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                name, x, y = parts[0], int(parts[1]), int(parts[2])
                nodes[name] = (x, y)
    return nodes

def determine_floor(sequence):
    """
    Determine the floor (piso) for each node in the sequence.

    Args:
        sequence: List of node names.

    Returns:
        A list of tuples (node_name, piso).
    """
    piso = None
    result = []
    floor0 = ["A", "B", "C", "S"]
    floor1 = ["Y", "W", "X", "U", "Z", "E"]
    for i, node in enumerate(sequence):
        if node[0].upper() in floor0:
            piso = 0
        elif node[0].upper() in floor1:
            piso = 1
        else:
            piso = int(node[0])  # Use the hundreds digit of the first node
        result.append((node, piso))
    return result

def draw_nodes_on_images(image_path_piso_0, image_path_piso_1, json_path, coordinates_path, output_path_piso_0="nodes_piso_0.png", output_path_piso_1="nodes_piso_1.png"):
    """
    Draw nodes on separate images for piso 0 and piso 1 based on a JSON sequence and coordinates file.

    Args:
        image_path_piso_0: Path to the image file for piso 0.
        image_path_piso_1: Path to the image file for piso 1.
        json_path: Path to the JSON file containing the sequence of node names.
        coordinates_path: Path to the coordinates file containing node coordinates.
        output_path_piso_0: Path to save the image with nodes drawn for piso 0.
        output_path_piso_1: Path to save the image with nodes drawn for piso 1.
    """
    try:
        # Load the images for piso 0 and piso 1
        img_piso_0 = Image.open(image_path_piso_0)
        img_piso_1 = Image.open(image_path_piso_1)
        draw_piso_0 = ImageDraw.Draw(img_piso_0)
        draw_piso_1 = ImageDraw.Draw(img_piso_1)

        # Load the JSON sequence
        with open(json_path, 'r') as f:
            data = json.load(f)
            sequence = [node['name'] for node in data['path']]

        # Parse the coordinates file
        nodes = parse_coordinates_file(coordinates_path)

        # Determine the floor for each node
        nodes_with_floors = determine_floor(sequence)

        # Draw the nodes and lines on the respective images
        previous_node = None
        for i, (node, piso) in enumerate(nodes_with_floors):
            if node in nodes:
                x, y = nodes[node]
                radius = 2.5

                # Determine the color for the node
                if i == 0:  # Start node
                    color = "green"
                    radius = 3.5
                elif i == len(nodes_with_floors) - 1:  # Finish node
                    color = "red"
                    radius = 3.5
                else:
                    color = "blue"
                    radius = 2.5

                # Draw the node on the appropriate image
                if piso == 0:
                    draw_piso_0.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=color)
                    if previous_node and previous_node[1] == 0:
                        prev_x, prev_y = nodes[previous_node[0]]
                        draw_piso_0.line((prev_x, prev_y, x, y), fill="blue", width=2)  # Draw a line
                elif piso == 1:
                    draw_piso_1.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=color)
                    if previous_node and previous_node[1] == 1:
                        prev_x, prev_y = nodes[previous_node[0]]
                        draw_piso_1.line((prev_x, prev_y, x, y), fill="blue", width=2)  # Draw a line

                previous_node = (node, piso)

        # Save the modified images
        img_piso_0.save(output_path_piso_0)
        img_piso_1.save(output_path_piso_1)
        print(f"Nodes drawn and saved to {output_path_piso_0} and {output_path_piso_1}")
    except FileNotFoundError:
        print("Error: Image, JSON, or coordinates file not found.")
    except KeyError:
        print("Error: 'path' key not found in JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")
