import heapq

class KthLarget:
    def __init__(self, k, nums):
        self.k = k
        self.maxheap = [-score for score in nums]
        heapq.heapify(self.maxheap)

    def add(self, val):
        heapq.heappush(self.maxheap, -val)
        sorted_val = sorted(self.maxheap)
        return -sorted_val[(self.k-1)]