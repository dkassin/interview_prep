# Notes, I purposely returned an array, and then the number for debugging
# I know that fi

def fibonacci_number(x: int):
    array = []
    while x > len(array):
        if len(array) < 2:
            array.append(1)
        else:
            number = array[-1] + array[-2]
            array.append(number)
    return array, array[x-1]

print(fibonacci_number(3))
print(fibonacci_number(5))
print(fibonacci_number(8))
print(fibonacci_number(10))