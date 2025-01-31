def running_sum(nums):
    running_sum = None
    for i in range(len(nums)):
        if running_sum == None:
            running_sum = [nums[i]]
        else:
            sum_val = running_sum[i-1] + nums[i]
            running_sum.append(sum_val)
    return running_sum

assert running_sum([1,2,3,4]) == [1,3,6,10]
assert running_sum([1,1,1,1,1]) == [1,2,3,4,5]
assert running_sum([3,1,2,10,1]) == [3,4,6,16,17]
