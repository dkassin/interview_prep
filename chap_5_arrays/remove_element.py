def remove_element(nums,val) -> int:
    count_of_val = nums.count(val)
    for _ in range(count_of_val):
        nums.pop(nums.index(val))
    print(nums)
