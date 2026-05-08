from factory import ConverterFactory

class ConverterApp:

    def process(self, text, choice):

        converter = ConverterFactory.create(choice)

        if not converter:
            raise ValueError("Converter tidak ditemukan")

        return converter.convert(text)

    def run(self):

        print("=== PROGRAM TEXT CONVERTER ===")

        while True:

            print("\nPilihan Converter:")
            print("1. upper")
            print("2. lower")
            print("3. binary")

            text = input("\nMasukkan text : ")
            choice = input("Pilih converter : ")

            try:

                result = self.process(text, choice)

                print("\nHasil Convert:")
                print(result)

            except ValueError as e:
                print("Error:", e)

            again = input("\nConvert lagi? (y/n): ")

            if again.lower() != "y":
                break
