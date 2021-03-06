""" Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2], your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4], your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

[0,0,1,1,1,2,2,3,3,4]


[1, 1, 2] -> [1, 2]
"""

def remove_duplicates(nums: list) -> int:

    for i in range(len(nums) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if nums[j] == nums[i]:
                del nums[j]

    return nums

test1 = [1, 1, 2]
test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


print(remove_duplicates(test2))