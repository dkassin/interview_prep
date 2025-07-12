def is_palindrome(head) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    second_list = prev
    while second_list:
        if second_list.val != head.val:
            return False
        second_list = second_list.next
    return True