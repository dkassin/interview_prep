def game_results(head) -> str:
    current = head
    even, odd = 0,0 
    
    while current and current.next:
        if current.val > current.next.val:
            even += 1
        elif current.next.val > current.val:
            odd += 1
        current = current.next.next
    
    if even > odd:
        return "Even"
    elif odd > even:
        return "Odd"
    else:
        return "Tie"