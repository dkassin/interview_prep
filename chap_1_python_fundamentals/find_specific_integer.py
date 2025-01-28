def find_specific_integer():
    for i in range (10000,100000):
        a,b,c,d,e = str(i)
        if i % 2 != int(a):
            continue
        elif i % 3 != int(b):
            continue
        elif i % 4 != int(c):
            continue
        elif i % 5 != int(d):
            continue
        elif i % 6 != int(e):
            continue
        return i
    
print(find_specific_integer())
