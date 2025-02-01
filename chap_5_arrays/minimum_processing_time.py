def min_processing_time(processor_time,tasks) -> int:
    tasks_sorted = sorted(tasks)
    reversed_processor = sorted(processor_time)[::-1]
    max = 0
    for index, value in enumerate(tasks_sorted):
        calc_value = reversed_processor[index//4] + value
        if max < calc_value:
            max = calc_value
    return max