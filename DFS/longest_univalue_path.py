def longest_univalue_path(root):
    max_path = 0
    def dfs(root):
        nonlocal max_path
        if not root: return
        left = dfs(root.left)
        right = dfs(root.right)

        left_path = right_path = 0
        if root.left and root.left.val == root.val:
            left_path = left + 1
        if root.right and root.right.val == root.val:
            right_path = right +1
        max_path = max(max_path, left_path + right_path)
        return max(left_path,right_path)
    dfs(root)
    return max_path