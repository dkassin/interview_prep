from sortedcontainers import SortedSet
class SmallestInfiniteSet:
    def __init__(self):
        self.infinite_set = SortedSet([i for i in range(1,1001)])

    def popSmallest(self):
        if len(self.infinite_set) > 0:
            value = self.infinite_set[0]
            self.infinite_set.remove(value)
            return value
    
    def addBack(self, num):
        if num not in self.infinite_set:
            self.infinite_set.add(num)
