
## First solution, it works but is not optimal
def find_nth_element(n: int):
    m = 1
    sequence = []
    while len(sequence) < n:
        for i in range(m):
            sequence.append(m)
        m += 1
    
    print(sequence[n-1])

find_nth_element(3)
find_nth_element(8)
find_nth_element(2050)


