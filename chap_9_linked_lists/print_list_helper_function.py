def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

    