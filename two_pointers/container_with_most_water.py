def container_with_most_water(heights):
    left, right = 0, len(heights)-1
    max_value = 0
    while left < right:
        area = min(heights[left],heights[right]) * (right - left)
        if area > max_value:
            max_value = area
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_value

assert container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49
assert container_with_most_water([1,1]) == 1
assert container_with_most_water([1,2,1]) == 2
assert container_with_most_water([4,3,2,1,4]) == 16


