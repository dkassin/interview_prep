def three_sum(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    value = [nums[i],nums[j],nums[k]]
                    value.sort()
                    if value not in result:
                        result.append(value)
    return result

## This is a brute force method that is n^3 but works.
## This is optimal

def threeSum(nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right] == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return result