from __future__ import annotations

from requests import request

class Tree():

    def __init__(self, data: int, children: list["Tree"] = None) -> None:

        self.data = data
        if children: self.children = children
        else: self.children = []

    def getOddAverage(self) -> int:
        '''''
        returns the average of all the odd values contained inside the Tree. If there are no odd values
        this method will return 0.
        '''''
        
        return self.getOddSum()/self.getOddCount()

    def getOddSum(self) -> int:
        sum = 0 

        if self.data % 2 != 0: sum = self.data

        for child in self.children:
            sum += child.getOddSum()

        return sum

    def getOddCount(self) -> int:
        count = 0

        if self.data % 2 != 0: count += 1

        for child in self.children:
            count += child.getOddCount()

        return count

if __name__ == "__main__":

    t2 = Tree(2, [Tree(5), Tree(6)])
    t3 = Tree(3, [Tree(7)])
    t = Tree (1, [t2, t3, Tree(4)])
    print(t.getOddSum())
    print(t.getOddCount())
    print(t.getOddAverage())