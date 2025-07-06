def min_swaps(data):
    start = 0
    one_count = sum(data)
    window_sum = 0
    max_ones = float('-inf')

    for end in range(len(data)):
        window_sum += data[end]

        if end - start +1 > one_count:
            window_sum -= data[start]
            start += 1

        if end - start +1 == one_count:
            max_ones = max(max_ones, window_sum)
    return one_count - max_ones