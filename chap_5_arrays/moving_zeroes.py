def moving_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    locate_zeros = []
    non_zeros = []
    for index, value in enumerate(nums):
        if nums[index] == 0:
            locate_zeros.append(index)
        else:
            non_zeros.append(value)

    for i in range(0,len(locate_zeros)):
        nums[-(i+1)] = 0
    for i in range(0,len(non_zeros)):
        nums[i] = non_zeros[i]
    
    print(nums)

    ## My solution theoretically works it does use extra space.
    ## The actual solution i needed help from chatgpt but it was very clever

    def move_zeroes_2(nums):
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1
            
        for i in range(position,len(nums)):
            nums[i] = 0

        print(nums)