class Node:
    def __init__(self, value, arr_num):
        self._value = value
        self._arr_num = arr_num
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        self._left = val

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        self._right = val


class Tree:
    def __init__(self):
        self._root = None

    def add(self, node: Node):
        if self._root is None:
            self._root = node
            return

        current_node = self._root

        while True:
            if node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = node
                    break
                else:
                    current_node = current_node.right


# Complete the triplets function below.
def triplets(a, b, c):
    tree = Tree()
    for val in a:
        tree.add(Node(val, 1))

    for val in b:
        tree.add(Node(val, 2))

    for val in c:
        tree.add(Node(val, 3))


lenaLenbLenc = input().split()

lena = int(lenaLenbLenc[0])

lenb = int(lenaLenbLenc[1])

lenc = int(lenaLenbLenc[2])

arra = list(map(int, input().rstrip().split()))

arrb = list(map(int, input().rstrip().split()))

arrc = list(map(int, input().rstrip().split()))