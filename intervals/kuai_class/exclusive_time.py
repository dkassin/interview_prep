def exclusive_time(n, logs):
    stack = []
    result = [0]*n
    prev_time = 0
    for i in logs:
        id,action,time = i.split(":")
        id = int(id)
        time = int(time)

        if action == 'start':
            if stack:
                result[stack[-1]] += time - prev_time
            stack.append(id)
            prev_time = time
        else:
            result[stack.pop()] += time - prev_time +1
            prev_time = time +1
    return result