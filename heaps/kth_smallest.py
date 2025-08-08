import heapq

def kth_smallest(matrix, k) -> int:
    max_heap = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            heapq.heappush(max_heap,-matrix[i][j])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
    return -max_heap[0]