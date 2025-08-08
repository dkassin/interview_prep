from collections import deque
def width_of_binary_tree(root):
    if not root:return max_width
    max_width = 0
    queue = deque([(root,0)])
    while queue:
        level_size = len(queue)
        _, first_index = queue[0]
        end_index= -1
        for i in range(level_size):
            node, index = queue.popleft()
            if i == level_size - 1:
                end_index = index
            if node.left:
                queue.append((node.left), 2*index)
            if node.right:
                queue.append((node.right, 2 * index + 1))
        max_width = max(max_width, end_index - first_index + 1)
    return max_width