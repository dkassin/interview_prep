from collections import deque
def zigzag_level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    count = 0
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr = queue.popleft()
            current_level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        count += 1
        if count % 2 == 0:
            result.append(current_level[::-1])
        else:
            result.append(current_level)
    return result