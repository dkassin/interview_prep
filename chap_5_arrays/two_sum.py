def two_sum(nums, target):
    for i in range(len(nums)):
            number = target - nums[i]
            if number in nums[i+1:]:
                print(f"number value {number}, i value {i}, nums plus {nums[i+1:]}")
                index_val = (i+1) + nums[i+1:].index(number)
                return [i, index_val]
            
    ## This solution works but i should come back and look at the hash solution

def two_sum_2(nums, target):
    hash = {}

    for index, value in enumerate(nums):
        number = target - value
        if number in hash:
            return [hash[number],index ]
        else:
            hash[value] = index

               
    