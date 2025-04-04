def minLength(s) -> int:
    stack = []
    bad = ["AB", "CD"]
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue

        value = f'{stack[-1]}{i}'
        if value in bad:
            stack.pop()
            continue

        stack.append(i)
    
    return len(stack)

assert minLength("ABFCACDB") == 2
assert minLength("ACBBD") == 5