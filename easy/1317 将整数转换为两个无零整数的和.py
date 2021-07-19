'''
「无零整数」是十进制表示中 不含任何 0 的正整数。给你一个整数 n，请你返回一个由两个整数
组成的列表 [A, B]，满足：A 和 B 都是无零整数  A + B = n
题目数据保证至少有一个有效的解决方案。
如果存在多个有效解决方案，你可以返回其中任意一个。
示例 1：输入：n = 2 输出：[1,1] 
解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。
示例 2：输入：n = 11 输出：[2,9]
示例 3：输入：n = 10000 输出：[1,9999]
示例 4：输入：n = 69  输出：[1,68]
示例 5：输入：n = 1010  输出：[11,999]
提示：2 <= n <= 10^4
'''

def getNoZeroIntegers(n):
    s = [int(x) for x in str(n)]
    l = len(s)
    if l == 1:
        return [n - 1, 1]
    A, B = [], []
    for i in range(l - 1):
        v = s[- i - 1]
        b = 1 if v != 1 else 2
        a = v - b
        if a < 0:
            a += 10
            s[- i - 2] -= 1
        A = [a] + A
        B = [b] + B
    if s[0] != 0:
        A = [s[0]] + A
    return [int(''.join([str(x) for x in A])),
            int(''.join([str(x) for x in B]))]
    
print(getNoZeroIntegers(2))
print(getNoZeroIntegers(19))
print(getNoZeroIntegers(11))
print(getNoZeroIntegers(10000))
print(getNoZeroIntegers(69))
print(getNoZeroIntegers(1010))

#92.82
#5.52



