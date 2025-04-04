def removeDuplicates(self, s: str) -> str:
    stack = []
    for char in s:
        if len(stack) < 1:
            stack.append(char)
            continue
        
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)