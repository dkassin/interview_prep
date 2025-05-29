def contains_duplicate(nums) -> bool:
    num_set = set(nums)
    if len(nums) != len(num_set):
        return True
    return False


assert contains_duplicate([1,2,3,1]) == True
assert contains_duplicate([1,2,3,4]) == False
assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True