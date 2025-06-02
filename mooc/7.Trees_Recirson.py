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