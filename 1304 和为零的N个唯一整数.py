'''
给你一个整数 n，请你返回任意一个由n个 各不相同 的整数组成的数组，并且这n个数相加和为0。
示例 1： 输入：n = 5  输出：[-7,-1,1,3,4] 
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
示例 2：输入：n = 3  输出：[-1,0,1]
示例 3：输入：n = 1  输出：[0]
提示： 1 <= n <= 1000
'''

def sumZero(n):
    ans = []
    for i in range(1, n // 2 + 1):
        ans.extend([-i, i])
    if n % 2 != 0:
        ans.append(0)
    return ans
        
print(sumZero(5))
print(sumZero(3))
print(sumZero(1))

#96.34
#8.23