def find_tilt(root):
    count = 0
    def dfs(root):
        nonlocal count
        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)
        tilt = abs(left - right)
        count += tilt
        return left + right + root.val
    dfs(root)
    return count