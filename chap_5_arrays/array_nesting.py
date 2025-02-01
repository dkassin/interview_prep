def array_nesting(nums):
    max_len = 0
        
    for i in range(len(nums)) :
        used = {}
        num = nums[i]
        
        while num not in used:
            temp = num
            num = nums[temp]
            used[temp] = 1

        max_len = max(max_len,len(used))
    return max_len

## Does not work on all solutions with extreme examples, had to look at chatgpt for optimal solution

def array_nesting_optimal(nums):
    max_len = 0

    for i in range(len(nums)):
        if nums[i] != -1:  # Only process unvisited elements
            start = i
            count = 0

            while nums[start] != -1:  # Traverse until we hit a visited node
                temp = start
                start = nums[start]
                nums[temp] = -1       # Mark as visited by modifying nums in-place
                count += 1

            max_len = max(max_len, count)

    return max_len