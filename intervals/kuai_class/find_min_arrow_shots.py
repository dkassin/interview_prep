def find_min_arrow_shots(points):
    points.sort(key=lambda x:x[1])
    arrows = 0
    last_shot = float('-inf')
    for start,end in points:
        if start > last_shot:
            arrows += 1
            last_shot = end
    return arrows