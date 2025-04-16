from google import genai
from google.genai import types
import json


class Gemini:

    def __init__(self, api_key: str, model:str):
        try:
            self.client = genai.Client(api_key=api_key)
            self.model = model

            with open("allEdges.txt", "r") as file:
                self.graph = file.read()

            self.output_rules = {  
                "type": "ARRAY",
                "items": {
                    "type": "STRING"
                },
            }

        except Exception as e:
            print(f"Error in Gemini initialization: {e}")
            raise
        

    def getPath(self, start: str, end: str) -> dict:

        """
        Generates a path between two points using the Gemini model.
        :param start: Starting point for the path.
        :param end: Ending point for the path.
        :return: a json file containing the path point's coordinates.

        """


        try:
            prompt = f"""A tua missão é encontrar o menor caminho entre 2 nós de um grafo.
                     O grafo é bidirecional e está representado pela seguinte lista de arestas:

                     {self.graph}

                     Deves retornar a lista que contém os nós do caminho.
                     É imperativo que utilizes apenas as arestas que estão apresentes na lista de acima.
                     
                     Encontra o menor caminho entre os nós {start} e {end}.
                     Se não houver caminho, retorna uma lista vazia."""


            response = self.client.models.generate_content(

                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.0,
                    response_mime_type="application/json",
                    response_schema= self.output_rules
                )
                
            )

        except Exception as e:
            print(f"Error in getPath: {e}")
            return None

        return response.parsed



    def listToJson(self, list):
        """
        Converts a list to a JSON string in the specified format.
        :param list: The list to convert.
        :return: A JSON string in the format:
                {
                    "path": [
                        {"name": "string"},
                        {"name": "string"},
                        ...
                    ]
                }
        """
        try:
            formatted = {"path": [{"name": item} for item in list]}  # Format the list
            return json.dumps(formatted, indent=4)  # Convert to JSON string with indentation
        except Exception as e:
            print(f"Error converting list to JSON: {e}")
            return None
