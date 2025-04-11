import requests
from chatai import ChatAI


class OllamaChatAI(ChatAI):
    def get_response(self, user_prompt: str) -> str:
        """ Get response from Ollama model.
        This method sends a request to the Ollama API with the user's prompt
        and retrieves the generated response.
        It uses the Mistral model for generating responses.

        Args:
            user_prompt (str): The user's input prompt.

        Returns:
            str: The AI's response.
        """
        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "mistral",
            "prompt": user_prompt,
            "stream": False
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("response")
        else:
            return f"Error: {response.status_code} {response.text}"


ai = OllamaChatAI()

# Bucle principal de interacción con el usuario
print("Inicia la conversación con la IA (escribe 'exit' para salir).")
while True:
    print("Input: ", end="")
    user_input = input()

    if user_input.lower() == "exit":
        break  # Salir del bucle si el usuario escribe 'exit'

    # Obtener y mostrar la respuesta de la IA
    ai_response = ai.get_response(user_input)
    print("Response: ", ai_response)

print("Saliendo del programa.")
