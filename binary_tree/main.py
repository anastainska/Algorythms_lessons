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

# Print the tree
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.value),
        if self.right:
            self.right.printtree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)


root.printtree()
