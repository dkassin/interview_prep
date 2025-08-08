def get_intersection_node(headA, headB):
    seen = set()
    while headA:
        seen.add(headA)
        headA = headA.next
    while headB:
        if headB in seen:
            return headB
        headB = headB.next
    return None