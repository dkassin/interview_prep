def max_score(cards, k):
    state = 0
    start = 0
    max_points = 0
    total = sum(cards)
    if k >= len(cards):
        return total

    for end in range(len(cards)):
        state += cards[end]

        if end - start + 1 == len(cards) - k:
            max_points = max(max_points, total-state)
            state -= cards[start]
            start += 1
    return max_points

assert max_score([1,2,3,4,5,6,1],3) == 12
assert max_score([9,7,7,9,7,7,9],7) == 55
assert max_score([1,79,80,1,1,1,200,1],3) == 202

