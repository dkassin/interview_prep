def three_sum_closest(nums,target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            sum_value = nums[left] + nums[right] + nums[i]
            if abs(sum_value - target) < abs(closest- target):
                closest = sum_value
            
            if sum_value > target:
                right -= 1
            elif sum_value < target:
                left += 1
            else:
                return sum_value
    return closest
