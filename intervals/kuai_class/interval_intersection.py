def interval_intersection(firstList, secondList):
    i,j = 0,0
    result = []
    while i < len(firstList) and j < len(secondList):
        a_start, a_end = firstList[i]
        b_start, b_end = secondList[j]
        max_start = max(a_start,b_start)
        min_end = min(a_end, b_end)

        if max_start <= min_end:
            result.append([max_start,min_end])
        
        if a_end < b_end:
            i += 1
        else:
            j += 1
    return result