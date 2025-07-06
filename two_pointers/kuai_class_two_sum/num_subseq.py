def num_subseq(nums,target):
    nums.sort()
    count = 0
    left = 0
    right = len(nums)-1
    mod = 10**9 +7

    while left <= right:
        if nums[left] + nums[right] <= target:
            count += 2**(right - left)
            left += 1
        else:
            right -= 1
    return (count % mod)