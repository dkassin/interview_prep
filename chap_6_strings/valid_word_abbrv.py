def valid_word_abbrev(word: str, abbr: str) -> bool:
    i , j = 0,0

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False
            
            nums = 0
            while j < len(abbr) and abbr[j].isdigit():
                nums = nums * 10 + int(abbr[j])
                j += 1

            i += nums
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return len(word) == i and len(abbr) == j
