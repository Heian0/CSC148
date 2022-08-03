from pet import Pet

class Cat(Pet):

    def __init__(self, name: str):
        super().__init__(name)

    def play(self) -> None:
        if not self.awake: return
        print("meow")