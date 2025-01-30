def subtract_product_and_sum(n: int) -> int:
    sum_val = sum([int(i) for i in str(n)])
    prod = 0
    for index, value in enumerate(str(n)):
        if index < 1:
            prod = int(value)
        else:
            prod = int(value) * prod
    return prod - sum_val