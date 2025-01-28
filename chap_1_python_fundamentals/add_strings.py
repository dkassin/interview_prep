
def add_strings(num1, num2):
    sum = get_int_value(num1) + get_int_value(num2)
    print(str(sum))

def get_int_value(num):
    num_list = list(num)
    total_number = 0
    reversed_list = num_list[::-1]
    for digit, number in enumerate(reversed_list):
        # Apparently i can get rid of the loop by using ord for calcuting the strings
        for i in range(0,10):
            if number == str(i):
                new_number = pow(10, digit) * i
                total_number += new_number
    return total_number

    # val = len(num)
    # start = pow(10,val-1)
    # end = pow(10,val)
    # for i in range(start, end):
    #     if str(i) == num:
    #         return i

# print(get_int_value("111"))
# get_int_value("111")
add_strings("0","9")