# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_second_minimum_value(root: TreeNode) -> int:
    min_val = set()
    def dfs(node):
        if not node:
            return
        min_val.add(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    if len(min_val) < 2:
        return -1
    
    return sorted(min_val)[1]