def diameter_of_binary_tree(root):
    max_diameter = 0
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        max_diameter = max(max_diameter, left+right)
        return max(left,right) +1
    dfs(root)
    return max_diameter