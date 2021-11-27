'''
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...,
nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经
旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值
是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
示例 1：输入：nums = [2,5,6,0,0,1,2], target = 0 输出：true
示例 2：输入：nums = [2,5,6,0,0,1,2], target = 3 输出：false
提示： 1 <= nums.length <= 5000 -10^4 <= nums[i] <= 10^4
题目数据保证 nums 在预先未知的某个下标上进行了旋转  -10^4 <= target <= 10^4
进阶：
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''

def search(nums, target):
    l, r = 0, len(nums) - 1
    v_l, v_r = nums[l], nums[r]
    while l + 1 < r:
        m = (l + r) // 2
        v_m = nums[m]
        if v_m == target:
            return True
        if v_m == v_r:
            r -= 1
            v_r = nums[r]
        elif v_m < v_r:
            if v_m <= target <= v_r:
                l, v_l = m, v_m
            else:
                r, v_r = m, v_m
        elif v_m > v_r:
            if v_l <= target <= v_m:
                r, v_r = m, v_m
            else:
                l, v_l = m, v_m
    if target in [v_l, v_r]:
        return True
    else:
        return False
    
    
print(search([2, 5, 6, 0, 0, 1, 2], 0))
print(search([2, 5, 6, 0, 0, 1, 2], 3))
print(search([1, 0, 1, 1, 1], 0))
print(search([1, 1, 1, 1, 2, 1, 1], 2))
print(search([1, 1, 2, 1, 1, 1, 1], 2))

#88.02
#60.10