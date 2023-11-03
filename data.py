def setZeroes(matrix):
   if not matrix:
      return []

   rows , cols = len(matrix),len(matrix[0])
   zero_rows, zero_cols = set(), set()

   for row in range(rows):
      for col in range(cols):
         if matrix[row][col]==0:
            zero_rows.add(row)
            zero_cols.add(col) 
            print(zero_cols)
            print(zero_rows)





matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
result = setZeroes(matrix)
