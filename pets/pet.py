class Pet():
    """""
    A class representing a real world pet.
    name (name of the pet): str 
    toys (toys that this pet has): list[str] -> default []
    awake (is the pet awake): bool -> default True
    """""

    def __init__(self, name : str, toys : list = []) -> None:
        self.name = name
        self.toys = toys
        self.awake = True

    def __str__(self) -> str:
        return "{0}, Collection: {1}, Sleeping: {2}". format(self.name, str(self.toys), not self.awake)

    def __len__(self) -> int:
        """""
        input -> self: Pet
        output -> length of self.toys: int
        """""
        return len(self.toys)

    def rest(self) -> None:
        self.awake = False

    def take(self, toy) -> None:
        """""
        input -> toy: str
        """""
        if not self.awake: self.awake = True
        self.toys.append(toy)

    def play(self) -> None:
        raise NotImplementedError

    