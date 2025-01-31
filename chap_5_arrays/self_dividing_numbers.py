def self_dividing_numbers(left,right):
    return [i for i in range(left,right+1) if is_self_dividing(i)]

def is_self_dividing(number):
    digit_list = set(str(number))
    if '0' in digit_list:
        return False
    
    for i in digit_list:
        if number % int(i) != 0:
            return False
    return True



assert self_dividing_numbers(1,22) == [1,2,3,4,5,6,7,8,9,11,12,15,22]
assert self_dividing_numbers(47,85) == [48,55,66,77]