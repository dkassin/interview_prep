def ispalindrome(n: int) -> bool:
    n_to_str = str(n)
    reversed_n = n[::-1]
    if n_to_str == reversed_n:
        return True
    else:
        return False
    
# Kuai way, return the conditional

def is_palindrome(n: int) -> bool:
    n_str = str(n)
    return n_str == n_str[::-1]
