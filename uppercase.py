from converter import Converter

class UpperCase(Converter):

    def convert(self, text: str) -> str:
        return text.upper()
