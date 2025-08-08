import heapq

## This uses a max heap
def kth_largest(nums, k):
    heap = [-i for i in nums]
    heapq.heapify(heap)

    for _ in range(k):
        result = heapq.heappop(heap)
    return -result 

## This uses a min heap
def kth_largest(nums, k):
    min_heap = []
    heapq.heapify(min_heap)
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

