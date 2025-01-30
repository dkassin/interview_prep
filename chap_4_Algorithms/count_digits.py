def count_digits(num: int) -> int:
    collection = [i for i in str(num) if num % int(i) == 0]
    return len(collection)