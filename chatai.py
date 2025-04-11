from abc import ABC, abstractmethod


class ChatAI(ABC):
    @abstractmethod
    def get_response(self, user_prompt: str) -> str:
        pass
