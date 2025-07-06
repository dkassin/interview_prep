from collections import defaultdict

def longest_substring(s,k):
    state = defaultdict(int)
    start = 0
    max_val = float('inf')

    for end in range(len(s)):
        state[s[end]] += 1

        while all(value >= k for value in state.values()):
            max_val = max(max_val, end-start+1)
            state[s[start]] -= 1
            start += 1
    return max_val

## This doesn't work, and chatgpt says it cant be solved properly with sliding window
### Ask kuai about this