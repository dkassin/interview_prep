def score_of_parenthesis(s):
    stack = []
    for char in s:
        if char == '()':
            stack.append(char)
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                total = 0
                while stack and isinstance(stack[-1], int):
                    total += stack.pop()
                stack.pop()
                stack.append(2* total)
    return sum(stack)