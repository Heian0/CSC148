from pet import Pet
from dog import Dog
from cat import Cat

if __name__ == "__main__":

    friend1 = Cat('Gilbert')
    print(friend1)
    friend2 = Dog('Teddy')
    print(friend2)
    friend1.take('mouse')
    print(friend1)
    print(len(friend1))
    friend2.take('bone')
    print(friend2)
    print(len(friend2))
    friend1.rest()
    print(friend1)
    friend2.rest()
    print(friend2)
    friend1.play()
    friend1.take('string')
    print(friend1)
    friend1.play()
    friend2.play()
    print(friend2)
    friend2.play()
    friend2.play()

