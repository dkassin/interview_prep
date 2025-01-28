def prime_number_checker(x: int) -> bool:
    if x == 1:
       return False
    if x in [2,3]:
       return True
    
    if x % 2 == 0:
        return False
    
    midpoint = (x // 2)
    for i in range(3,midpoint,2):
       if x % i == 0:
        return False
        
    return True
    

print(prime_number_checker(3))
print(prime_number_checker(24689))
print(prime_number_checker(29))
print(prime_number_checker(12))