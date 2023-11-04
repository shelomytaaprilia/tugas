class Camel_case:
    def __init__(self, word:str):
        self.word = word

    def __str__(self):
        return f"{self.word}"

    def printData(self):
        print(f"------------**------------")
        print(f"{saya.word}")
        print(f"--------------------------")
        print(f"{saya.word}".split(" "))
        print(f"--------------------------")
        print(f"{saya.word}".title())
        print(f"------------**------------")

saya = Camel_case("saya suka kamu")
saya.printData()