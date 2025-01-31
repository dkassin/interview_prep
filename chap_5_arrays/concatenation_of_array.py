def get_concatenation(nums):
    return [i for i in nums] * 2

assert get_concatenation([1,2,1]) == [1,2,1,1,2,1]
assert get_concatenation([1,3,2,1]) == [1,3,2,1,1,3,2,1]