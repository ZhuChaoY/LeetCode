'''
给你一个整数数组A，请你给数组中的每个元素A[i]都加上一个任意数字x（-K <= x <= K），
从而得到一个新数组B。返回数组 B 的最大值和最小值之间可能存在的最小差值。
示例 1： 输入：A = [1], K = 0 输出：0 解释：B = [1]
示例 2： 输入：A = [0,10], K = 2 输出：6 解释：B = [2,8]
示例 3： 输入：A = [1,3,6], K = 3 输出：0 解释：B = [3,3,3] 或 B = [4,4,4]
提示： 1 <= A.length <= 10000 0 <= A[i] <= 10000  0 <= K <= 1000
'''

def smallestRangeI(nums, k):
    return max(0, max(nums) - min(nums) - 2 * k)
    
print(smallestRangeI([1], 0))
print(smallestRangeI([0, 10], 2))
print(smallestRangeI([1, 3, 6], 3))

#90.33
#82.55