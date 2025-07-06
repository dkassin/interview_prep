## From collections import deque
def max_sum(nums, k):
    state = []
    ## use deque([])
    start = 0
    max_value = 0
    for end in range(len(nums)):
        state.append(nums[end])
        if end - start + 1 == k:
            if len(set(state)) == k:
                value = sum(state)
                max_value - max(max_value, value)
            state.pop(0)
            # popleft()
            start += 1
    return max_value

max_sum([4,2,4,5,6],4) == 17
max_sum([1,2,3,4,5],2) == 9
max_sum([5,5,5,5,5],3) == 0
max_sum([1,1,1,1,1],1) == 1

## This is not an optimal solution, because arrays are not the optimal data type.
## If going to use arrays could use deque with popleft to be faster
from collections import defaultdict
def optimal_max_sum(nums,k):
    state = defaultdict(int)
    max_value = 0
    start = 0
    distinct = 0
    current_value = 0

    for end in range(len(nums)):
        value = nums[end]
        current_value += value
        state[value] += 1

        if state[value] == 1:
            distinct += 1

        if end - start + 1 == k:
            if distinct == k:
                max_value = max(max_value,current_value)

            state[nums[start]] -= 1
            if state[nums[start]] == 0:
                distinct -= 1

            
            current_value -= nums[start] 
            start += 1
    return max_value