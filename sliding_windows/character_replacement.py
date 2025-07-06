def character_replacement(s:str, k: int):
    state = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0)+1
        while ((end-start+1) - max(state.values())) > k:
            state[s[start]] -= 1
            start += 1
        max_length = max(max_length, end - start +1)
    return max_length

assert character_replacement('ABAB',2) == 4
assert character_replacement('AABABBA',1) == 4
assert character_replacement('ABCDE',1) == 2
assert character_replacement('AAABBBCCC',3) == 6

## slighty more elegant solution

def character_replacement(s,k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0)+1
        max_freq = max(max_freq, state[s[end]])

        if k + max_freq < end - start + 1:
            state[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start +1)
    return max_length