def clear_digits(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue
            
        if i.isdigit():
            stack.pop()
            continue

        stack.append(i)
    return ''.join(stack)

assert clear_digits("abc") == "abc"
assert clear_digits("cb34") == ""