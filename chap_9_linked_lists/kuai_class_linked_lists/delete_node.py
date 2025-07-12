# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def delete_node(self, node):
    node.val = node.next.val
    node.next = node.next.next