def decode_cipher_text(encodedText: str, rows:int) -> str:
    cols = int(len(encodedText) / rows)
    matrix = [[0] * cols for _ in range(rows)]
    encoded_text_array = [char for char in encodedText]
    encoded_text_array.reverse()
    
    for i in range(rows):
        for j in range(cols):
            value = encoded_text_array.pop()
            matrix[i][j] = value
    
    result = []

    for start_col in range(cols):
        x, y = 0, start_col
        while x < rows and y < cols:
            result.append(matrix[x][y])
            x += 1
            y += 1

    return "".join(result).rstrip()