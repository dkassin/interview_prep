# Problem 1 Collatz Conjecture
def collatz_conjecture(x):
    tracker = []
    while x != 1:
        tracker.append(x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = (x * 3) + 1
    return len(tracker)
print(collatz_conjecture(3))
print(collatz_conjecture(7))
print(collatz_conjecture(13))
print(collatz_conjecture(20))

assert collatz_conjecture(3) == 7
assert collatz_conjecture(7) == 16
assert collatz_conjecture(13) == 9
assert collatz_conjecture(20) == 7