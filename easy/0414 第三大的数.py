'''
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。
要求算法时间复杂度必须是O(n)。
示例 1: 输入: [3, 2, 1] 输出: 1
示例 2: 输入: [1, 2]  输出: 2 解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3: 输入: [2, 2, 3, 1] 输出: 1
'''

def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.remove(max(nums))
    nums.remove(max(nums))
    return max(nums)

print(thirdMax([3, 2, 1]))
print(thirdMax([2, 1]))
print(thirdMax([3, 2, 2, 1]))
        
#49.79
#44.70
