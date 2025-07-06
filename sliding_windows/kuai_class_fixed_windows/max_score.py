def max_score(cardPoints,k):
    max_points = sum(cardPoints)
    if k >= len(cardPoints):
        return max_points
    window_size = len(cardPoints)-k
    start = 0
    min_total = float('inf')
    state = 0

    for end in range(len(cardPoints)):
        state += cardPoints[end]

        if end - start +1 == window_size:
            min_total = min(min_total, state)
            state -= cardPoints[start]
            start += 1
    return max_points - min_total