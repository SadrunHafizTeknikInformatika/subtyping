from converter import Converter

class LowerCase(Converter):

    def convert(self, text: str) -> str:
        return text.lower()
