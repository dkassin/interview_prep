def has_cycle(head)-> bool:
    slow, fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return False
    return True