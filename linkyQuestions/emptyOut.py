from __future__ import annotations

class Node():

    def __init__(self, data: int, next = None) -> None:

        self.data = data
        self.next = next

class LinkedList():

    def __init__(self, items: list["int"]):

        if len(items) == 0:
            self._first = None

        else:
            self._first = Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = Node(item)
                curr = curr.next

    def __str__(self) -> str:

        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def emptyOut(self) -> int:

        if self._first == None:

            return 0

        total = 0
        curr = self._first.next
        while curr:
            total = total + curr.data
            curr = curr.next

        self._first.next = None

        return total


if __name__ == "__main__":

    linky1 = LinkedList([1, 2, 3, 4, 5, 9, 69])
    linky2 = LinkedList([])

    print(linky1.emptyOut())
    print(linky2.emptyOut())
    print(linky1)
    print(linky2)




