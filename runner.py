from prompter import Gemini
from draw import draw_nodes_on_images
from flask import Flask, request, jsonify


app = Flask(__name__)  # Create a Flask app
@app.route('/generate-map', methods=['POST'])  # Define a route for the path endpoint
def main():
    data = request.get_json()  # Get the JSON data from the request
    start = data.get("start")  # Get the start node from the request data
    end = data.get("end")  # Get the end node from the request data

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
    output_file_piso_0 = "public/generated/nodes_piso_0.png"  # Output file for piso 0
    output_file_piso_1 = "public/generated/nodes_piso_1.png"  # Output file for piso 1
    
    draw_nodes_on_images(image_file_piso_0, image_file_piso_1, json_file, coordinates_file, output_file_piso_0, output_file_piso_1)
    return jsonify({"status": "ok", "images": ["generated/nodes_piso_0.png", "generated/nodes_piso_1.png"]})

if __name__ == "__main__":
    app.run(port=5000)  # Run the Flask app on port 5000
    main("entrance", "008")