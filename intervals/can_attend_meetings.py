def can_attend_meetings(intervals):
    intervals.sort(key=lambda x:x[0])
    prev_interval = None
    # optimize, prev_interval = interval[0]
    for i in intervals:
    # optimize, for i in intervals[1:]
        if prev_interval == None:
            prev_interval = i
        ## in optimization can remove lines 7/8 and set up logic to start
        elif prev_interval[1] > i[0]:
            return False
        prev_interval = i
    return True

assert can_attend_meetings([[0,30],[5,10],[15,20]]) == False
assert can_attend_meetings([[7,10],[2,4]]) == True
assert can_attend_meetings([[1,2],[2,3],[3,4]]) == True
assert can_attend_meetings([[1,3],[2,4],[4,6]]) == False