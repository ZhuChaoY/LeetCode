'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
示例 1：输入：nums = [5,7,7,8,8,10], target = 8  输出：[3,4]
示例 2：输入：nums = [5,7,7,8,8,10], target = 6  输出：[-1,-1]
示例 3：输入：nums = [], target = 0 输出：[-1,-1]
提示：0 <= nums.length <= 10^5 -10^9 <= nums[i] <= 10^9
nums 是一个非递减数组   -10^9 <= target <= 10^9
'''

def searchRange(nums, target):
    if nums == []:
        return [-1, -1]
    
    l, r = 0, len(nums) - 1
    L = -1
    while l + 1 < r:
        m = (l + r) // 2
        v_m = nums[m]
        if v_m < target:
            l = m
        else:
            r = m
            if v_m == target:
                L = m           
    if target == nums[r]:
        L = r
    if target == nums[l]:
        L = l
        
    l, r = 0, len(nums) - 1
    R = -1
    while l + 1 < r:
        m = (l + r) // 2
        v_m = nums[m]
        if v_m > target:
            r = m
        else:
            l = m
            if v_m == target:
                R = m 
    if target == nums[l]:
        R = l
    if target == nums[r]:
        R = r
        
    return [L, R]

    
print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([5, 8, 8, 8, 8, 10], 8))
print(searchRange([1], 1))
print(searchRange([1, 1], 1))
print(searchRange([], 0))

#58.21
#88.26
