def longest_substring_without_repeat(s: str):
    state = {}
    start = 0
    max_string = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) +1

        while any(v > 1 for v in state.values ()):
            state[s[start]] -= 1
            if state[s[start]] == 0:
                del state[s[start]]
            start += 1

        max_string = max(max_string, end - start +1)
    return max_string

assert longest_substring_without_repeat("abcabcbb") == 3
assert longest_substring_without_repeat("eghghhgg") == 3
assert longest_substring_without_repeat("") == 0
assert longest_substring_without_repeat("substring") == 8

### EVEN BETTER SOLUTION

def longest_substring_without_repeat(s: str):
    state = {}
    start = 0
    max_string = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) +1

        ## This cleverly checks the most recent increment which is the only one that can change this condition
        while state[s[end]] > 1:
            state[s[start]] -= 1
            ## Dont need to delete bc we aren't checking length were checking a value
            start += 1
        max_string = max(max_string, end - start +1)
    return max_string



## Best Solution 
### Instead of taking counts this tracks indexes, tricker but very elegant

def longest_substring_without_repeat(s):
    state = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in state:
            ## if index was recorded then it's a duplicate and we move the start to index after last occurance
            start = max(start, state[s[end]]+1)

        state[s[end]] = end
        max_length = max(max_length, end - start +1)
    return max_length