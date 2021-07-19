'''
给定一个整数 n，返回 n! 结果尾数中零的数量。
输入: 3 输出: 0 解释: 3! = 6, 尾数中没有零。
输入: 5 输出: 1 解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
'''

def trailingZeroes(n):
    ans = 0
    while n > 0:
        n //= 5
        ans += n 
    return ans
    
print(trailingZeroes(3))
print(trailingZeroes(5))    
print(trailingZeroes(10))  
print(trailingZeroes(50))    
    
#75.18
#94.47 