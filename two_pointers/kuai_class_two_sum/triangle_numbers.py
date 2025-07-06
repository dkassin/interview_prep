## My first attempt:
## Does not work
### Only works if there are non-repeating numbers

def triangle_numbers(nums):
    count = 0
    nums.sort()
    for i in range(len(nums)-1,1,-1):
        if nums[i] >= nums[i-1] >= nums[i-2] and (nums[i-2] + nums[i-1]) > nums[i]:
                count += 1
    return count

## The working solution
def triangle_number(nums):
    count = 0
    nums.sort()
    for i in range(len(nums)-1,1,-1):
         left = 0
         right = i-1
         while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right-left)
                right -= 1
            else:
                 left += 1
    return count
                   