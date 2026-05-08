from converter import Converter

class BinaryText(Converter):

    def convert(self, text: str) -> str:
        return ' '.join(format(ord(c), '08b') for c in text)
