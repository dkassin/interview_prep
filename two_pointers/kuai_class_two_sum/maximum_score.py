## This is a valid brute force solution

def maximum_score(nums,k):
    max_score = float('-inf')
    for i in range(k+1):
        for j in range(k,len(nums)):
            if i <= k <= j:
                value = min(nums[i:j+1]) * (j - i +1)
                max_score = max(max_score,value)
    return max_score

## Optimal solution
### The key is starting at key and using two pointers to work outward
### We must track the minimum value using a variable to keep it o(n)

def maximum_score(nums,k):
    max_score = float('-inf')
    min_value = nums[k]
    i,j = k,k
    while i >= 0 and j <= len(nums)-1:
        min_value = min(min_value, nums[i],nums[j])
        max_score = max(max_score, min_value*(j-i+1))
        if i == 0:
            j += 1
        elif j == len(nums)-1:
            i -=1
        else:
            if nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1
    return max_score