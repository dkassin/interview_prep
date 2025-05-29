from collections import Counter
def is_anagram(s, t) -> bool:
    s_counter, t_counter = Counter(s),Counter(t)
    return s_counter == t_counter

assert is_anagram(s ="anagram", t = "nagaram") == True
assert is_anagram(s ="rat", t = "car") == False
