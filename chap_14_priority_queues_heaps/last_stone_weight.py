import heapq
def last_stone_weight(stones) -> int:
    heap = []
    for i in stones:
        heapq.heappush(heap, -i)
    
    while len(heap) > 1:
        y,x = -heapq.heappop(heap), -heapq.heappop(heap)
        if y != x:
            heapq.heappush(heap,-(y-x))
    
    if len(heap) > 0:
        return -heap[0]
    return 0