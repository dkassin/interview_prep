# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
    prev, current = None, head
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current  = temp
    return prev