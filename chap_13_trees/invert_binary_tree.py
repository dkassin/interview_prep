class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return root