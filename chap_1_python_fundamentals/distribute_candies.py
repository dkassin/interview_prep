## First Solution

def distributeCandies(self, n: int, limit: int) -> int:
        hash = {}
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    hash[tuple([i,j,k])] = i+j+k 
        solution_array = []
        for key,value in hash.items():
            if value == n:
                for i in key:
                    check = []
                    if i <= limit:
                        check.append(True)
                if all(check):
                    solution_array.append(key)
        return len(solution_array)

## Improved Solution

def distribute_candies(n: int, limit: int):
    hash = {}
    for i in range(limit+1):
        for j in range(limit+1):
            for k in range(limit+1):
                if (i+j+k) == n: 
                    hash[tuple([i,j,k])] = 0
                else:
                    continue
                
    solution_array = []
    for key in hash.items():
        if all([
            key[0][0] <= limit,
            key[0][1] <= limit,
            key[0][2] <= limit,
        ]):
            solution_array.append(key)

## Final Improved Solution

def distribute_candies(n: int, limit: int):
    solution_array = set([])
    for i in range(limit+1):
        for j in range(limit+1):
            for k in range(limit+1):
                if (i+j+k) == n: 
                    if i <= limit and j <= limit and k <= limit:
                        solution_array.add(tuple([i,j,k]))
         
    print(len(solution_array))

distribute_candies(5,2)
distribute_candies(3,3)
    