from collections import defaultdict
def total_fruit(fruits):
    state = defaultdict(int)
    start = 0
    max_val = 0
    for end in range(len(fruits)):
        state[fruits[end]] += 1

        while len(state) > 2:

            state[fruits[start]] -= 1
            if state[fruits[start]] == 0:
                del state[fruits[start]]
            start += 1
        max_val = max(sum(state.values()), max_val)
    return max_val

