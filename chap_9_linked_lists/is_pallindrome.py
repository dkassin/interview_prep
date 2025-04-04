# Brute force solution that is slow

def is_palindrome(head):
    original = deepcopy(head)
    prev, current = None, head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    reversed_head = prev
    while original and reversed_head:
        if original.val != reversed_head.val:
            return False
        original = original.next
        reversed_head.next

    return True


def is_palindrome_2(head):
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
        head = head.next
    
    return True