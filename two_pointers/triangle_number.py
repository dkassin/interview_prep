def triangle_number(heights):
    count = 0
    heights.sort()
    for i in range(len(heights)-1,1,-1):
        left = 0
        right = i-1
        while left < right:
            if heights[left]+heights[right] > heights[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1
    return count