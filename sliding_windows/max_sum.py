def max_sum(nums,k):
    state = 0
    start = 0
    max_val = 0

    for end in range(len(nums)):
        state += nums[end]

        if (end-start+1) == k:
            max_val = max(max_val, state)
            state -= nums[start]
            start += 1
        
    return max_val

assert max_sum([4,2,4,5,6],4) == 17
assert max_sum([1,2,3,4,5],2) == 9
assert max_sum([1,2,1,3,1,1,1],3) == 6
assert max_sum([5,5,5,5,5],3) == 15