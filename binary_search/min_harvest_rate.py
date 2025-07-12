import math

def min_harvest_rate(apples, h):
    apples.sort()
    left = 1
    right = apples[-1]

    while left <= right:
        mid = (right + left) // 2
        total_hours = sum(math.ceil(a/ mid) for a in apples)
        if total_hours <= h:
            right = mid - 1
        else:
            left = mid +1
    return left