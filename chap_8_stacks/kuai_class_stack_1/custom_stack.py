class CustomStack:

    def __init__(self, maxSize:int):
        self.maxSize = maxSize
        self.stack = []
        self.length = 0

    def push(self, x:int) -> int:
        if self.length < self.maxSize:
            self.stack.append(x)
            self.length +=1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        else:
            self.length -= 1
            return self.stack.pop()
        
    def increment(self, k: int, val: int) -> None:
        if self.length <= k:
            self.stack = [i + val for i in self.stack]
        else:
            for i in range(k):
                self.stack[i] += 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)