def has_path_sum(root, target_sum) -> bool:
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        if target_sum == root.val:
            return True
    
    target_sum -= root.val
    left = has_path_sum(root.left, target_sum)
    right = has_path_sum(root.right, target_sum)

    return left or right