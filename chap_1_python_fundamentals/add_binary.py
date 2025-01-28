def addBinary( a: str, b: str) -> str:
    sum = convert_to_number(a) + convert_to_number(b)
    return bin(sum)[2:]


def convert_to_number(str):
        reverse = str[::-1]
        count = 0
        
        for index, i in enumerate(reverse):
            count += (pow(2,index) * int(i))
        return count
        
print(addBinary("11","1"))
print(addBinary("1010","1011"))
