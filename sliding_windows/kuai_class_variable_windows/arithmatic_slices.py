def number_of_arithmatic_slices(nums):
    if len(nums) < 3:
        return 0
    total = 0
    curr = 0

    for i in range(2,len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            curr += 1
            total += curr
        else:
            curr = 0
    return total