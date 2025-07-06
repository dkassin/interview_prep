from collections import defaultdict
def car_pooling(trips,capacity):
    events = defaultdict(int)
    for cap,start,end in trips:
        events[start] += cap
        events[end] -= cap

    current_load = 0
    for time in sorted(events):
        current_load += events[time]
        if current_load > capacity:
            return False
    return True    