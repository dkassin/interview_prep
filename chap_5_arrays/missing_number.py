def missing_number(nums) -> int:
    max_sum = sum([i for i in range(len(nums)+1)])
    return max_sum - sum(nums)

assert missing_number([3,0,1]) == 2
assert missing_number([0,1]) == 2
assert missing_number([9,6,4,2,3,5,7,0,1]) == 8