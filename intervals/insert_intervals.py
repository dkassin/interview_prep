def insert_intervals(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key = lambda x: x[0])
    result = [intervals[0]]

    for i in intervals[1:]:
        if i[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], i[1])
        else:
            result.append(i)

    return result

assert insert_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]