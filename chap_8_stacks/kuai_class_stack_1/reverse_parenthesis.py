def reverse_parenthesis(s):
    stack = []
    for char in s:
        if char == ")":
            current_string = []
            while stack[-1] != '(':
                current_string.append(stack.pop())
            stack.pop()
            stack.extend(current_string)
        else:
            stack.append(char)
    return "".join(stack)