def rotate_strings(s: str,goal: str) -> bool:
    return len(s) == len(goal) and goal in (s+s)

    # from collections import deque
    #  This solution is really clever
    # I initially thought about add the first letter of s to the end and then checking the ord values
    # This is better just add both and then look for the value in the other value


