class Node:
    def __init__(self, given):
        self.root = given
        self.left = None 
        self.right = None
temp = [*range(1,10)]
root = Node(10)
while len(temp)<1:
    root.left = temp.pop()
    root.right = temp.pop()
    