def add_digits(num):
    array = list(str(num))
    while len(array) > 1:  
        number = 0 
        for i in array:
            number += int(i)
        array = list(str(number))
    return int(array[0])

print(add_digits(38))