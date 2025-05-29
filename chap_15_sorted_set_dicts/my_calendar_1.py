from sortedcontainers import SortedSet
class myCalendar:
    def __init__(self):
        self.order_book = SortedSet([])

    def book(self, startTime, endTime):
        if len(self.order_book) == 0:
            self.order_book.add((startTime, endTime))
            return True
        
        for x,y in self.order_book:
            if not (startTime >= y or endTime <= x):
                return False
        
        self.order_book.add((startTime, endTime))
        return True