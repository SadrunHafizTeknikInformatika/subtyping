from uppercase import UpperCase
from lowercase import LowerCase
from binarytext import BinaryText

class ConverterFactory:

    @staticmethod
    def create(choice):

        converters = {
            "upper": UpperCase(),
            "lower": LowerCase(),
            "binary": BinaryText()
        }

        return converters.get(choice.lower())
