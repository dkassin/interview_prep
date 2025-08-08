## Brute Force Solution doesn't pass

def sumSubarrayMins(arr) -> int:
        n = len(arr)
        result = 0
        for i in range(n):
            min_val = arr[i]
            for j in range(i,n):
                print(min_val,arr[j], i, j)
                min_val = min(min_val, arr[j])
                result += min_val
        return result % (10**9+7)


### Lets go over this with Kuai