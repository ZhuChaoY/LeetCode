'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）
的长度。 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1：输入：nums = [100,4,200,1,3,2]  输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2： 输入：nums = [0,3,7,2,5,8,4,6,0,1] 输出：9
提示： 0 <= nums.length <= 10^5  -10^9 <= nums[i] <= 10^9
'''


def longestConsecutive(nums):
    ans = 0
    D = {}
    for num in nums:
        if num not in D:
            D[num] = 0
            if num - 1 in D:
                left = D[num - 1]
            else:
                left = 0
            if num + 1 in D:
                right = D[num + 1]
            else:
                right = 0
            length = left + right + 1
            D[num - left] = length
            D[num + right] = length
            ans = max(ans, length)    
    return ans
            
    
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([4, 0, -4, -2, 2, 5, 0, -8, -1, 7, 4, 5, -4, 6, -3]))

#29.53
#15.89