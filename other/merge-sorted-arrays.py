# Given two sorted arrays, the task is to merge them in a sorted manner.

# Examples:

# Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8}
# Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

# Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
# Output: arr3[] = {4, 5, 7, 8, 8, 9}

# input1: [1, 5, 6, 7]
# input2: [2, 8, 9, 10]


def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    k = 0
    new = [None] * (len(arr1) + len(arr2))


    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new[k] = arr1[i]
            i += 1
            k += 1
        elif arr2[j] < arr1[i]:
            new[k] = arr2[j]
            j += 1
            k += 1

    while j < len(arr2):
        new[k] = arr2[j]
        j += 1
        k += 1
    
    while i < len(arr1):
        new[k] = arr1[i]
        i += 1

    return new



test1 = [1, 3, 4, 5]
test2 = [2, 4, 6, 8]
test11 = [1, 3, 4, 5, 6, 8, 9, 14, 15, 16, 23]
test22 = [0, 2, 5, 7, 7, 7, 8, 9, 16, 17, 20]


print(merge_sorted_arrays(test11, test22)) # 1 -> 2

# iterate arrays
# if array1[idx] < array2[idx] and array1[idx] < array1[idx + 1]
    # append array1[idx]
# if array1[idx] < array2[idx] and array2[idx] > array1[idx + 1]
    # append array1[idx + 1]
