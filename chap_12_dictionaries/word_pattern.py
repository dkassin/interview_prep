def word_pattern(pattern: str, s: str) -> bool:
    track_hash = {}
    word2_array = s.split(" ")
    if len(word2_array) != len(pattern):
        return False
    
    for word1, word2 in zip(pattern, word2_array):
        if word1 not in track_hash:
            if word2 in track_hash.values():
                return False
            track_hash[word1] = word2
        elif track_hash[word1] != word2:
            return False
    return True

assert word_pattern(pattern = "abba", s = "dog cat cat dog") == True
assert word_pattern(pattern = "abba", s = "dog cat cat fish") == False
assert word_pattern(pattern = "aaaa", s = "dog cat cat dog") == False