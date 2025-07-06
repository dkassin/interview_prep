import heapq
def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x:x[0])
    heap = []
    for i in intervals:
        if heap and i[0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, i[1])
    return len(heap)