def reverse_string(s):
    """
        Do not return anything, modify s in-place instead.
    """
    pointer_left = 0
    pointer_right = len(s) - 1
    while pointer_left <= pointer_right:
        s[pointer_left],s[pointer_right] = s[pointer_right],s[pointer_left]
        pointer_left += 1
        pointer_right -= 1
    ## Return statement is only there for assertions to pass
    return s

assert reverse_string(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert reverse_string(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]