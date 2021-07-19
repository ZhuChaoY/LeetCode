'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中
，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。
输入: [1,3,5,6], 5 输出: 2
输入: [1,3,5,6], 2 输出: 1
输入: [1,3,5,6], 7 输出: 4
输入: [1,3,5,6], 0 输出: 0
'''

def searchInsert(nums, target):
    n = len(nums)
    nums.append(target + 1)
    for i in range(n):
        if nums[i] >= target:
            return i
        elif nums[i + 1] >= target:
            return i + 1
    
print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))  
print(searchInsert([1], 0))          

#74.77
#21.06