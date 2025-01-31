def second_largest_element(nums) -> int:
    large_element_array = None
    for i in nums:
        if large_element_array == None:
            large_element_array = [i]
        elif len(large_element_array) < 2:
            if large_element_array[0] >= i:
                large_element_array.append(i)
            else:
                temp = large_element_array[0]
                large_element_array = [i, temp]
        else:
            if i > large_element_array[0]:
                large_element_array.insert(0,i)
            elif i > large_element_array[1]:
                large_element_array.insert(1,i)
    return large_element_array[1]

nums1 = [1,2,4,3,645,6456,45645]
nums2 = [1231,123,5234234,223,12]
# print(second_largest_element(nums1))
assert second_largest_element(nums1) == 6456
assert second_largest_element(nums2) == 1231
assert second_largest_element([12, 35, 1, 10, 34, 1]) == 34
assert second_largest_element([100, 50, 100]) == 100