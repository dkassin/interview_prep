from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.events_1 = SortedDict()
        self.events_2 = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        curr_index = self.events_1.bisect_right(startTime)
        for start,end in self.events_2:
            if not (endTime <= start or startTime >= end):
                return False

        if curr_index > 0:
            prev_start,prev_end = self.events_1.peekitem(curr_index - 1)
            if prev_end > startTime:
                overlap_start = max(prev_start, startTime)
                overlap_end = min(prev_end, endTime)
                self.events_2.add((overlap_start,overlap_end))

        if curr_index < len(self.events_1):
            next_start, next_end = self.events_1.peekitem(curr_index)
            if endTime > next_start:
                next_overlap_start = max(next_start, startTime)
                next_overlap_end = min(next_end, endTime)
                self.events_2.add((next_overlap_start,next_overlap_end))

        
        self.events_1[startTime] = endTime
        print(self.events_2)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)