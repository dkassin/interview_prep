## My solution, only beat 17.68%

def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append((char,1))
            else:
                if stack[-1][0] == char:
                    if stack[-1][1] == k-1:
                        for _ in range(k-1):
                            stack.pop()
                    else:
                        stack.append((char,stack[-1][1]+1))
                else:
                    stack.append((char, 1))
        return "".join([a for a,b in stack])    

## Optimal Solution
def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # each element is [char, count]
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        return ''.join(char * count for char, count in stack)


