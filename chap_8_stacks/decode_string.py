def decond_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char is '[':
            stack.append(current_string)
            stack.append(current_number)
            current_string = ""
            current_number = 0
        elif char is ']':
            num = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + num * current_string
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            current_string += char
    return current_string