'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
输入: nums = [-1,0,3,5,9,12], target = 9 输出: 4
解释: 9 出现在 nums 中并且下标为 4
输入: nums = [-1,0,3,5,9,12], target = 2 输出: -1
解释: 2 不存在 nums 中因此返回 -1
你可以假设 nums 中的所有元素是不重复的。 n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''

def search(nums, target):
    if nums[0] == target:
        return 0
    elif nums[-1] == target:
        return len(nums) - 1
    l, r = 0, len(nums) - 1
    while l < r - 1:
        m = (l + r) // 2
        if nums[m] > target:
            r = m
        elif nums[m] < target:
            l = m
        else:
            return m
    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
print(search([-1, 0, 3, 5, 9, 12], 12))
print(search([-1, 0, 3, 5, 9, 12], -1))
print(search([-1, 0, 3, 5, 9, 12], -2))        
print(search([-1, 0, 3, 5, 9, 12], 13))        
        
#97.34
#5.22   