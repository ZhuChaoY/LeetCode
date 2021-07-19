'''
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 
n - 1 个元素增加 1。
输入: [1,2,3] 输出: 3 解释: 只需要3次移动（注意每次移动会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

def minMoves(nums):
    ans, Min = 0, min(nums)
    for num in nums:
        ans += num - Min
    return ans
    
print(minMoves([1, 2, 3]))

#78.91
#76.08
