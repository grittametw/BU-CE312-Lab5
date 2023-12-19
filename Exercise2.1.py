class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if(node.data < root.data):
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

root = Node(50)
insert(root, Node(25))
insert(root, Node(75))
insert(root, Node(30))
insert(root, Node(60))
insert(root, Node(40))