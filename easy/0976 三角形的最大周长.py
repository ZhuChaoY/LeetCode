'''
给定由正数（代表长度）组成的数组A，返回由三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。
示例 1： 输入：[2,1,2] 输出：5 
示例 2： 输入：[1,2,1] 输出：0
示例 3： 输入：[3,2,3,4] 输出：10
示例 4： 输入：[3,6,2,3] 输出：8
提示： 3 <= A.length <= 10000 1 <= A[i] <= 10^6
'''

def largestPerimeter(nums):
    n = len(nums)
    nums = sorted(nums)[::-1]
    for i in range(2, n):
        a, b, c = nums[i - 2], nums[i - 1], nums[i]
        if a < b + c:
            return a + b + c
    return 0
                    
print(largestPerimeter([2, 1, 2]))
print(largestPerimeter([1, 2, 1]))
print(largestPerimeter([3, 2, 3, 4]))
print(largestPerimeter([3, 6, 2, 3]))

#99.30
#42.91
