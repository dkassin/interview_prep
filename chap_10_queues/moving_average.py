from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
    
    def next(self, val:int) -> float:
        self.queue.append(val)
        if len(self.queue) < self.size:
            return sum(self.queue) / len(self.queue)
        else:
            self.queue.popleft()
            return sum(self.queue) / self.size
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

## Question for Kuai 
### This solution, passed, and it is very readable and easy to understand
### Yet it was no where near the optimal solution, is this valid?

## Also 