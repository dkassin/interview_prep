# This harder problem only allows data stores with constant time, so nothing that grows
## That makes it so you cannot use hashes
### I also solved this in a nested loop but it times out

def two_sum_2(numbers, target):
    left = 0
    right = len(numbers)-1
    while left <= right:
        value = numbers[left] + numbers[right]
        if value  == target:
            return [left+1,right+1]
        if value > target:
            right -= 1
        else:
            left += 1