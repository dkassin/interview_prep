from collections import Counter
def unique_occurrences(arr) -> bool:
    valid_hash = {}
    counts = Counter(arr)
    for count in counts.values():
        if count in valid_hash:
            return False
        else:
            valid_hash[count] = 1
    return True

assert unique_occurrences([1,2,2,1,1,3]) == True
assert unique_occurrences([1,2]) == False
assert unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True