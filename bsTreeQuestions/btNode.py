class BTNode():

    def __init__(self, data: int, 
                left: "BTNode" = None, 
                right: "BTNode" = None) -> None:

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:

        return 'BTNode({0}, {1}, {2})'.format(self.data, repr(self.left), repr(self.right))

    def mutate(self, depth):

        if self.left: self.left.mutate(depth)
        if self.right: self.right.mutate(depth)

        if self.data < depth:
            temp = self.left
            self.left = self.right
            self.right = temp
        
        else: self.data = self.data + depth

if __name__ == "__main__":

    bt1 = BTNode(2, BTNode(5), BTNode(6))
    bt2 = BTNode(3, BTNode(7), BTNode(0))
    btTest = BTNode(1, bt1, bt2)
    print(btTest)
    btTest.mutate(3)
    print(btTest)