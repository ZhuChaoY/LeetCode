'''
给定一个二进制数组， 计算其中最大连续1的个数。
输入: [1,1,0,1,1,1] 输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
输入的数组只包含 0 和1。输入数组的长度是正整数，且不超过 10,000。
'''

def findMaxConsecutiveOnes(nums): 
    k, ans = 0, 0
    for num in nums:
        if num == 1:
            k += 1
        else:
            if k > 0:
                ans = max(ans, k)
                k = 0
    return max(ans, k)

print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
                
#85.44                
#54.09  
