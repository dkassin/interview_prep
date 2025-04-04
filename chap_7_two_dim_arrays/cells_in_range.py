def cells_in_range(s: str):
    a,b = s.split(":")
    array = []
    for i in range(ord(a[0]),ord(b[0])+1):
        array.append(chr(i))
    output = []
    for j in array:
        for i in range(int(a[1]),int(b[1])+1):
            output.append(j +str(i))
    return output

assert cells_in_range("K1:L2") == ["K1","K2","L1","L2"]

assert cells_in_range("A1:F1") == ["A1","B1","C1","D1","E1","F1"]