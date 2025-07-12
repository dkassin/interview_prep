def min_remove_to_make_valid(s):
    stack = []
    freq = 0

    for char in s:
        if char == "(":
            stack.append(char)
            freq += 1
        elif char == ")":
            if freq > 0:
                stack.append(char)
                freq -= 1
        else:
            stack.append(char)
    result = []

    for char in reversed(stack):
        if char == '(' and freq > 0:
            freq -= 1
        else:
            result.append(char)
    return "".join(reversed(result))