import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    min_heap = []
    counter = 0
    for i in lists:
        while i:
            heapq.heappush(min_heap,(i.val,counter,i))
            counter += 1
            i = i.next
        dummy = ListNode(0)
        current = dummy
        
        for _ in range(len(min_heap)):
            _,_,node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
        current.next = None
        return dummy.next