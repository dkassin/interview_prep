def find_longest_chain(pairs):
    pairs.sort(key=lambda x:x[1])
    result = [pairs[0]]
    for i in pairs[1:]:
        if result[-1][1] < i[0]:
            result.append(i)
    return len(result)