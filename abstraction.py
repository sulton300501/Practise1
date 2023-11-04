def setZeroes(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    
    # Find rows and columns that contain zeros
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    # Set rows and columns to zero based on the zero_rows and zero_cols sets
    for row in zero_rows:
        for col in range(cols):
            matrix[row][col] = 0

    for col in zero_cols:
        for row in range(rows):
            matrix[row][col] = 0

    return matrix

# Example usage:
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
result = setZeroes(matrix)

# Print the result
for row in result:
    print(row)

