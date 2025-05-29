from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    magazine_count = Counter(magazine)
    for char in ransom_note:
        if char not in magazine_count or magazine_count[char] == 0:
            return False
        else:
            magazine_count[char] -= 1
    return True

assert can_construct(ransom_note = "a", magazine = "b") == False
assert can_construct(ransom_note = "aa", magazine = "ab") == False
assert can_construct(ransom_note = "aa", magazine = "aab") == True