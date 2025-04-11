from abc import ABC, abstractmethod


class ChatAI(ABC):
    @abstractmethod
    def get_response(self, user_prompt: str) -> str:
        """ 
        Abstract method to get a response from the AI model.
        Args:
            user_prompt (str): The user's input prompt.
        Returns:
            str: The AI's response.
        """
        pass
