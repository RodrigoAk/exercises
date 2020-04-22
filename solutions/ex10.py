'''
Given an integer k and a binary search tree, findthe floor
(less than or equal) of k, and the ceiling (larger than or equal to)
of k. If either does not exist, then print them as None.
'''


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    if(root_node is None):
        return (floor, ceil)

    if(root_node.value <= k):
        if(floor is not None):
            if(root_node.value > floor):
                floor = root_node.value
            else:
                return (floor, ceil)
        else:
            floor = root_node.value
    else:
        if(ceil is not None):
            if(root_node.value < ceil):
                ceil = root_node.value
            else:
                return (floor, ceil)
        else:
            ceil = root_node.value

    floor, ceil = findCeilingFloor(root_node.left, k, floor=floor, ceil=ceil)
    floor, ceil = findCeilingFloor(root_node.right, k, floor=floor, ceil=ceil)

    return (floor, ceil)


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
