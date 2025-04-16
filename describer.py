from google import genai
from google.genai import types

class Describer:

    def __init__(self, api_key: str, model:str):
        try:
            self.client = genai.Client(api_key=api_key)
            self.model = model

            self.output_rules = {  
                "type": "STRING"
            }

        except Exception as e:
            print(f"Error in Gemini initialization: {e}")
            raise

    def getDescription(self, path_piso0, path_piso1):

        """
        Generates a description of the path using the Gemini model.
        :param path_piso0: Path in piso 0.
        :param path_piso1: Path in piso 1.
        :return: a json file containing the path point's coordinates.

        """

        try:
            prompt = f"""A tua missão é descrever um caminho entre dois pontos de um grafo.
                        O caminho é representado pela linha azul. O ponto de partida é de cor VERDE e o ponto de chegada é de cor VERMELHA.
                        
                        Piso 0: {path_piso0}
                        Piso 1: {path_piso1}
                        
                        Deves retornar uma descrição do caminho, incluindo os pontos de partida e chegada, e as direções a seguir."""

            response = self.client.models.generate_content(

                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.0,
                    response_mime_type="application/json",
                    response_schema= self.output_rules
                )
            )

            return response.generated_content

        except Exception as e:
            print(f"Error in getDescription: {e}")
            raise