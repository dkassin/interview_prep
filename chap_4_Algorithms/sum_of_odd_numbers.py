def sum_of_odd_numbers(n: int) -> int:
    numbers_list = [i for i in range(1,n+1,2)] 
    return sum(numbers_list)

assert sum_of_odd_numbers(5) == 9
assert sum_of_odd_numbers(14) == 49