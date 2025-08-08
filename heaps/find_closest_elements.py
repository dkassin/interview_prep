import heapq
def find_closest_elements(arr, k, x):
    max_heap = []
    for i in arr:
        value = abs(i-x)
        heapq.heappush(max_heap, (-value,-i))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return sorted(-i[1] for i in max_heap)

## binary search or two pointers would actually be faster