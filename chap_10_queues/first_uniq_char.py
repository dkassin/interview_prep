from collections import Counter
def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1