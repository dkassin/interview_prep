def path_sum(root, target_sum):
    answer = []
    def dfs(root, target, tracker):
        nonlocal answer
        if not root:
            return
        
        tracker.append(root.val)
        if not root.left and not root.right and target == root.val:
            answer.append(list(tracker))

        left =dfs(root.left, target-root, tracker)
        right = dfs(root.right, target-root.val, tracker)

        tracker.pop()
    
    dfs(root,target_sum,[])
    return answer

## Simpler Answer
### Ask Kuai about this.
### The first answer is faster

def dfs(root, target):
    answer = []
    def dfs(root,target, tracker):
        if not root:
            return
        
        if not root.left and not root.right and target == root.val:
            answer.append(tracker + [root.val])
            return
        
        left = dfs(root.left, target - root.val, tracker + [root.val])
        right = dfs(root.right, target - root.val, tracker + [root.val])