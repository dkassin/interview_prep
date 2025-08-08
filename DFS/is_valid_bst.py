def is_valid_bst(root):
    def dfs(root,low,high):
        if root in None:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        left = dfs(root.left, low, root.val)
        right = dfs(root.right, root.val, high)

        return left and right

    return dfs(root, float('-inf'),float('inf'))