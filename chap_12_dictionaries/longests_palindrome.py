from collections import Counter
def longest_palindrome(s) -> int:
    counts = Counter(s)
    result = 0
    if len(counts.keys()) == 1:
        return counts[s[0]]
    
    for values in counts:
        counts_val = ((counts[values] // 2) * 2)
        result += counts_val
        counts[values] -= counts_val

    if 1 in counts.values():
        result += 1
    
    return result

assert longest_palindrome("abccccdd") == 7
assert longest_palindrome("a") == 1
assert longest_palindrome("bb") == 2
assert longest_palindrome("bananas") == 5
assert longest_palindrome("tattarrattat") == 12
assert longest_palindrome("ababababa") == 9