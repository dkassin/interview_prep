def plus_one(digits):
    number = 1
    for index,value in enumerate(reversed(digits)):
        value = pow(10,index) * value
        number += value
    return [int(i) for i in str(number)]

assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9]) == [1,0]