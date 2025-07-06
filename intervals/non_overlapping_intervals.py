def non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    merged = [intervals[0]]
    count = 0
    for i in intervals[1:]:
        if i[0] < merged[-1][1]:
            count += 1
        else:
            merged.append(i)
    return count

assert non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert non_overlapping_intervals([[1,2],[1,2],[1,2]]) == 2