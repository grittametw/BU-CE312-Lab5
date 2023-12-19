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
                   
def delete(root, node):
    if root is None:
        return root
    if node.data < root.data:
        root.left = delete(root.left, node)
    elif(node.data > root.data):
        root.right = delete(root.right, node)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        root.node = temp.node
        root.right = delete(root.right, temp.node)
    return root

def treeHeight(root):
    if root is None:
        return -1
    return max(treeHeight(root.left)+1, treeHeight(root.right)+1)

root = Node(50)
insert(root, Node(25))
insert(root, Node(75))
insert(root, Node(30))
insert(root, Node(60))
insert(root, Node(40))
delete(root, Node(30))
delete(root, Node(75))
delete(root, Node(40))
insert(root, Node(30))
insert(root, Node(75))
insert(root, Node(40))

print("Maximum height = ", treeHeight(root))
print("parent  = ")
print("children = ")
print("leaves  = ")
print("sibling = ")