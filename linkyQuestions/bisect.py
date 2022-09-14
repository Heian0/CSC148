from __future__ import annotations

class Node:

    def __init__(self, data: int, next = None) -> None:

        self.data = data
        self.next = next

def bisect(linky: "Node", index: int) -> "Node":
    if index < 0: raise IndexError
    if index == 0:
        temp = linky
        linky = Node(None)
        return temp

    cur_index = 0
    while linky and cur_index < index -1 :

        linky = linky.next
        cur_index += 1

    if cur_index == index - 1:

        temp = linky.next
        linky.next = None

        return temp

    else:

        raise IndexError

def displayLinky(linky: Node) -> str:

    linky_str = ""

    while linky and linky.next:
        linky_str = linky_str + str(linky.data) + " -> "
        linky = linky.next

    linky_str = linky_str + str(linky.data)

    return linky_str

if __name__ == "__main__":

    n3 = Node(4)
    n2 = Node(3, n3)
    n1 = Node(2, n2)
    linky = Node(1, n1)

    print(displayLinky(linky))
    linky2 = bisect(linky, 2)
    print(displayLinky(linky))
    print(displayLinky(linky2))


