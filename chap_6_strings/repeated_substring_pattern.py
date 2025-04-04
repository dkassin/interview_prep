def repeated_substring_pattern(s: str) -> bool:
    for i in range(1, len(s) // 2 +1):
        if len(s) % i == 0:
            word = s[:i]
            if word * (len(s) // i) == s:
                return True
    return False