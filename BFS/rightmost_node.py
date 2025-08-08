from collections import deque
def rightmost_node(nodes):
    if not nodes:return []
    result = []
    queue = deque([nodes])
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
        result.append(current_level[-1])
    return result