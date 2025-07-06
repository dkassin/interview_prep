def max_area(height):
    left = 0
    right = len(height)-1
    max_water = 0

    while left <= right:
        x_axis = right - left
        y_axis = min(height[left],height[right])
        max_water = max(max_water, (x_axis*y_axis))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water