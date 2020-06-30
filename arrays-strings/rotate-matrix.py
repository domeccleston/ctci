# def rotate_matrix(arr: list) -> list:
#     length = len(arr)
#     last = length - 1
#     new_arr = []

#     for i in range(length):
#         temp_arr = []
#         for j in range(last, -1, -1):
#             print(arr[j][i])
#             temp_arr.append(arr[j][i])
#         new_arr.append(temp_arr)
    
#     return new_arr

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
     [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# in place solution

# def rotate_matrix(matrix: list) -> list:
#     if len(matrix) == 0 or len(matrix) != len(matrix[0]):
#         return False

#     n = len(matrix)

#     for layer in range(int(n / 2)):
#         first = layer
#         last = n - 1 - layer
#         for i in range(last):
#             offset = i - first
#             top = matrix[first][i]
#             matrix[first][i] = matrix[last - offset][first]
#             matrix[last - offset][first] = matrix[last][last - offset]
#             matrix[last][last - offset] = matrix[i][last]
#             matrix[i][last] = top
    
#     return matrix

# print(rotate_matrix(m2))