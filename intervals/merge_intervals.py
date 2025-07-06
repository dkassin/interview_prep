def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in intervals[1:]:
        if merged[-1][1] >= i[0]:
            merged[-1][1] = max(i[1],merged[-1][1])
        else:
            merged.append(i)
    return merged

assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]