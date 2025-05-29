def is_isomorphic(s,t) -> bool:
    hash_check = {}
    hash_check_2 = {}
    for char_s, char_t in zip(s,t):
        if char_s not in hash_check:
            hash_check[char_s] = char_t
        elif hash_check[char_s] != char_t:
            return False
        
        if char_t not in hash_check_2:
            hash_check_2[char_t] = char_s
        elif hash_check_2[char_t] != char_s:
            return False
    return True