def next_greater_element(nums1,nums2):
    stack = []
    for i in range(len(nums1)):
        current_val = nums1[i]
        current_index = nums2.index(current_val)
        possible_vals = [i for i in nums2[current_index:] if i > current_val]
        if len(possible_vals) == 0:
            stack.append(-1)
        else:
            stack.append(possible_vals[0])
    return stack

assert next_greater_element([4,1,2],[1,3,4,2]) == [-1,3,-1]
assert next_greater_element([2,4],[1,2,3,4]) == [3,-1]


def next_greater_element_2(nums1,nums2):
    stack = []
    for i in range(len(nums1)):
        current_val = nums1[i]
        current_index = nums2.index(current_val)
        if len(nums2[current_index+1:]) == 0 or max(nums2[current_index+1:]) < current_val:
            stack.append(-1)
            continue
        
        for i in nums2[current_index+1:]:
                if i > current_val:
                    stack.append(i)
                    break
    return stack

# Lets go over an optimal solution for this and how you would arrive at it