class Tree:

    def init(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert(self.root, value)

class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.value),
        if self.right:
            self.right.printtree()


root = Node(24)
root.insert(17)
root.insert(32)
root.insert(30)
root.insert(13)
root.insert(18)


root.printtree()
