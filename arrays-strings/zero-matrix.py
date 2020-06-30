def zero_matrix(matrix):
    new_matrix = []
    zero_indices = []
    for i in range(len(matrix)):
        length = len(matrix[i])
        found_zero = False
        for j in range(length):
            if matrix[i][j] == 0:
                zero_indices.append(j)
                found_zero = True
                break
        if found_zero:
            new_matrix.append([0 for n in range(length)])
        else:
            new_matrix.append(matrix[i])

    for k in range(len(new_matrix)):
        for i in range(len(zero_indices)):
            new_matrix[k][zero_indices[i]] = 0

    return new_matrix

matrix1 = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# matrix2 = [
#     [1, 2, 3, 4],
#     [4, 5, 6, 7],
#     [7, 8, 9, 0],
#     ["a", 0, 0, 0]
# ]

print(zero_matrix(matrix1))
# print(zero_matrix(matrix2))