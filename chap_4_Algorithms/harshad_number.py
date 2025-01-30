def harshad_number(x: int) -> int:
    sum_val = sum([int(i) for i in str(x)])
    if x % sum_val == 0:
        return sum_val
    else: return -1