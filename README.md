### Ollama Interaction

ChatAI is a simple interface with a single method 'get_response(user_prompt: str) -> str' which returns the response for a provided user prompt. In the Ollama example we define a OllamaChatAPI class which inherits from the ChatAI class and overrides the get_response method to use the Ollama API to get the response.
