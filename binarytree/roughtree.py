class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Binary Tree Structure
#               1
#              / \
#             2   2
#            / \ 
#           3   3
#          / \
#         4   4

root = Node(1)
# b = Node(2)
# c = Node(2)
# d = Node(3)
# e = Node(3)
# f = Node(4)
# g = Node(4)

b=Node(2)
c=Node(3)

# root.left = b
# root.right = c
# b.left = d
# b.right = e
# d.left = f
# d.right = g
root.right=b 
b.right=c 


def bfs_traversal(rootNode):
    queue = [rootNode]
    values = []
    depth = 0  # Initialize depth as 0

    if rootNode is None:
        return values
    noDepth=list() # list keeps record of the endings in node at all levels 
    while len(queue) > 0:
        level_size = len(queue)
        depth += 1  # Increment depth at the start of each level
      # iterate through all nodes at the same level in bfs search
        for _ in range(level_size):
            current = queue.pop(0)
            values.append(current.value)
            if current==root:
                if current.left is None or current.right is None:
                    noDepth.append(depth)
            elif current.left is None and current.right is None:
                noDepth.append(depth)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

           

    return depth, values, noDepth # Return depth and values

depth, values, noDepth = bfs_traversal(root)
print("Depth of the binary tree:", depth)
print("BFS traversal values:", values)
print("different null values at different levels in bfs", noDepth)