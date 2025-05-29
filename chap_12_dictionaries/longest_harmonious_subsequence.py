from collections import Counter

def find_lhs(nums) -> int:
    counts = Counter(nums)
    max_val = 0
    for i in counts:
        value = counts.get(i+1, None)
        if value:
            if (counts[i] + value) > max_val:
                max_val = (counts[i] + value)
    return max_val


assert find_lhs([1,3,2,2,5,2,3,7]) == 5
assert find_lhs([1,2,3,4]) == 2
assert find_lhs([1,1,1,1]) == 0