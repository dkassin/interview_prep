def largest_perimeter(nums) -> int:
    # The sum of all sides exclusing the largest side must be greater then the largest side
    # This implementation works on nearly all test cases except extreme ones it times out
    sorted_list = sorted(nums)
    largest_perimeter = -1
    if len(nums) < 3:
        return -1
    for i in range(2,len(nums)):
        if sum(sorted_list[:i]) > sorted_list[i]:
            perimeter = sum(sorted_list[:i+1])
            if perimeter > largest_perimeter:
                largest_perimeter = perimeter
    return largest_perimeter

## This implementation passes all tests

    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        largest_perimeter = -1
        current_count = 0
        if len(nums) < 3:
            return -1
        for i in range(2,len(nums)):
            if largest_perimeter != -1:
                if current_count > sorted_list[i]:
                    perimeter = current_count + sorted_list[i]
                    current_count += sorted_list[i]
                    if perimeter > largest_perimeter:
                        largest_perimeter = perimeter
                else:
                    current_count += sorted_list[i]
            else:
                if sum(sorted_list[:i]) > sorted_list[i]:
                    perimeter = sum(sorted_list[:i+1])
                    current_count += perimeter
                    if perimeter > largest_perimeter:
                        largest_perimeter = perimeter

        return largest_perimeter
    
    ## Smart the best solutions reverse the list and work down from the largest numbers after sorting