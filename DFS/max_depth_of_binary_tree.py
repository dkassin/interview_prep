# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left,right) + 1

## Above is my solution works and follows the template
### Below is an optimized solution

def maxDepth(root):
    if root is None:
        return 0
    return 1+ max(maxDepth(root.left),maxDepth(root.right))