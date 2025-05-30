def spiral_matrix_3(rows:int, cols:int, rStart:int, cStart:int):
    result = []
    total = rows * cols
    r, c = rStart, cStart# right down left, up
    directions = [(0,1),(1,0), (0,-1), (-1,0)]
    step = 1
    result.append([r,c])
    while len(result) < (total):
        for i in range(4):
            dr, dc = directions[i]
            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r,c])
            if i % 2 == 1:
                step +=1
    result
