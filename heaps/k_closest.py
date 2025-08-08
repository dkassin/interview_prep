import heapq

def k_closest(points, k):
    max_heap = []
    for i in points:
        value = (i[0]**2) + (i[1]**2)
        heapq.heappush(max_heap, (-value,i))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    result = [i[1] for i in max_heap]
    return result