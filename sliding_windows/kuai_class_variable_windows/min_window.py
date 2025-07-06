from collections import defaultdict

def min_window(s,t):
    state = defaultdict(int)
    start = 0
    t_dict = defaultdict(int)
    for char in t:
        t_dict[char] += 1
    required = len(t_dict)
    formed = 0
    min_len = float('inf')
    min_start = 0

    for end in range(len(s)):
        value = s[end]
        state[value] += 1
        if value in t_dict and state[value] == t_dict[value]:
            formed += 1
        while formed == required:
            if end-start + 1 < min_len:
                min_len = end-start+1
                min_start = start
            state[s[start]] -= 1
            if s[start] in t_dict and state[s[start]] < t_dict[s[start]]:
                formed -=1
            start += 1
    return s[min_start:min_start+min_len] if min_len != float('inf') else ""


