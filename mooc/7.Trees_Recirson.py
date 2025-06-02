class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __repr__(self):
        return str(self.value)
    
node2 = Node(2)
node3 = Node(3)
node1 = Node(1, [node2, node3])

node = Node(1)
print(node)

tree = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])

#Traversing a tree - Recursion
def traverse(node):
    print("enter", node.value)
    for child in node.children:
        traverse(child)
    print("leave", node.value)

traverse(tree)

#Computing information from a tree
def count_nodes(node):
    result = 1
    for child in node.children:
        result += count_nodes(child)
    return result

print(count_nodes(tree))