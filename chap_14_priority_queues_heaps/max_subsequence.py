import heapq

def max_subsequence(nums, k):
    maxheap = [-number for number in nums]
    heapq.heapify(maxheap)
    result = []
    for i in range(k):
        value = heapq.heappop(maxheap)
        result.append(-value)
    return sorted(result)