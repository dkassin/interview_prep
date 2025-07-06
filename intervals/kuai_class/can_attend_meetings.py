def can_attend_meetings(intervals):
    if len(intervals) < 2:
        return True
    intervals.sort(key=lambda x:x[0])
    prev_interval = intervals[0]
    for i in intervals[1:]:
        if i[0] < prev_interval[1]:
            return False
        else:
            prev_interval = i
    return True