from pet import Pet

class Dog(Pet):

    def __init__(self, name: str, toys: list = ["ball"]) -> None:
        super().__init__(name, toys)

    def play(self) -> None:
        if not self.awake: self.awake = True
        if len(self.toys):
            print("Here is my {}! Play with me! Woof!!".format(self.toys.pop(0)))
            return
        print("I want to play! Arf arf!!")