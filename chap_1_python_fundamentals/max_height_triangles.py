def max_height_triangles(red,blue): 
    trial_array = [[red,blue], [blue, red]]
    result_array = []
    for i in trial_array:
        row_number = 0
        while (row_number % 2 == 0 and i[0] >= (row_number+1)) or (row_number % 2 != 0 and i[1] >= (row_number+1)):
            if row_number % 2 == 0 and i[0] >= (row_number+1):
                i[0] -= (row_number+1)
                row_number += 1
            elif row_number % 2 != 0 and i[1] >= (row_number+1):
                i[1] -= (row_number+1)
                row_number += 1
        result_array.append(row_number)
    return max(result_array)

print(max_height_triangles(2,4))
print(max_height_triangles(2,1))
print(max_height_triangles(1,1))
print(max_height_triangles(10,1))