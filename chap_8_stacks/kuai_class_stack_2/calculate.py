def calculate(s):
    stack = [0]
    number = 0

    for char in s.strip():
        if char == " ":
            continue
        if char.isdigit():
            number = number * 10 + int(char)
            if isinstance(stack[-1],int):
                stack.pop()
            stack.append(number)
        else:
            number = 0
            stack.append(char)
    
    new_stack = []
    i = 0
    while i < len(stack):
       while i < len(stack):
            if stack[i] == '*':
                new_stack[-1] = new_stack[-1] * stack[i + 1]
                i += 2
            elif stack[i] == '/':
                new_stack[-1] = int(new_stack[-1] / stack[i + 1])
                i += 2
            else:
                new_stack.append(stack[i])
                i += 1
     
    result = new_stack[0]
    i = 1
    while i < len(new_stack):
        if new_stack[i] == '+':
            result += new_stack[i + 1]
        elif new_stack[i] == '-':
            result -= new_stack[i + 1]
        i += 2
    
    return result