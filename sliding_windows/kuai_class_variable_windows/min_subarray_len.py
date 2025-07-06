def min_subarray_len(target, nums):
    start = 0
    state = 0
    min_length = float('inf')

    for end in range(len(nums)):
        state += nums[end]

        while state >= target:
            min_length = min(end-start+1,min_length)
            state -= nums[start]
            start += 1

    return 0 if min_length == float('inf') else min_length