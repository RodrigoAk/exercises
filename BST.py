class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))


def main():
    BST = TreeNode(5)
    BST.left = TreeNode(1)
    BST.right = TreeNode(6)
    BST.right.left = TreeNode(7)
    BST.right.right = TreeNode(8)

    if(Solution().isValidBST(BST)):
        print("É uma Binary Search Tree!")
    else:
        print("Não é uma Binary Search Tree!")


if(__name__ == "__main__"):
    main()
