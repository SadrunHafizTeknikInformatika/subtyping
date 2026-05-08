from abc import ABC, abstractmethod

class Converter(ABC):

    @abstractmethod
    def convert(self, text: str) -> str:
        pass
