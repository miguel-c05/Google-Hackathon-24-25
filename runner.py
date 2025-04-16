from prompter import Gemini
from draw import draw_nodes_on_images

def main(start, end):
    
    if start == "entrance":
        start = "C001"
        
    if end == "entrance":
        end = "C001"
    
    gemini = Gemini(api_key="AIzaSyB_dwm4WaSvc0ax3PaCF_C1QoI5FTK_ICU", model="gemini-2.5-pro-exp-03-25")
 
    response = gemini.getPath(start, end)
    json_response = gemini.listToJson(response)
    with open("path.json", "w") as json_file:
        json_file.write(json_response)

    image_file_piso_0 = "FC6_0.png"  # Replace with the actual path to your piso 0 image file
    image_file_piso_1 = "FC6_1.png"  # Replace with the actual path to your piso 1 image file
    json_file = "path.json"  # Replace with the actual path to your JSON file
    coordinates_file = "allNodes.txt"  # Replace with the actual path to your coordinates file
    output_file_piso_0 = "nodes_piso_0.png"  # Output file for piso 0
    output_file_piso_1 = "nodes_piso_1.png"  # Output file for piso 1
    
    draw_nodes_on_images(image_file_piso_0, image_file_piso_1, json_file, coordinates_file, output_file_piso_0, output_file_piso_1)


if __name__ == "__main__":
    main("entrance", "008")