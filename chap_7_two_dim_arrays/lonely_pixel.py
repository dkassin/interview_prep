def lonely_pixel(picture):
    rows, cols = len(picture), len(picture[0])
    rowCount = rows * [0]
    colCount = cols * [0]
    for row in range(rows):
        for col in range(cols):



picture = ["WWB", "WBW", "BWW"]
lonely_pixel(picture)

## Two types of problems, 
# 1. rotation or change the grid
## 2. Scan the grid

### 3. 

The first thing it to look at the parameters 


def is_loney(r,c):
        return (
             all(picture[r][j] == 'W' for j in range(n) if j!= c) and
             all(picture[i][class]] == 'W' for j in range(n) if j!= c)
        )


Bc implementation isnt strong, i should be implementing everything
return the datatype thats empty to see what your intermediate results are