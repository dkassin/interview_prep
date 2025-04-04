def rotate_image(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_matrix = len(matrix)
        for i in range(len_matrix):
            for j in range(i,len_matrix):
                print(f"{i,j} and {j,i}")
                #  This is add to be able to see the transformation that occurs
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in matrix:
            i.reverse()