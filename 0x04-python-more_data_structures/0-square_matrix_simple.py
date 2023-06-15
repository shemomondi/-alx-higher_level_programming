def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    result = [[0] * len(row) for row in matrix]
    
    # Iterate over the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square the value at each position and store it in the corresponding position of the result matrix
            result[i][j] = matrix[i][j] ** 2
    
    return result
