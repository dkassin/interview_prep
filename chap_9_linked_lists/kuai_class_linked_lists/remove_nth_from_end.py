class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head,n):
    count = 0
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current and current.next:
        current = current.next
        count += 1
    
    current = dummy
    for _ in range(count - n):
        current = current.next

    current.next = current.next.next
    return dummy.next
