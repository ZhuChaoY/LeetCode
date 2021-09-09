'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
示例 1：输入：x = 2.00000, n = 10 输出：1024.00000
示例 2：输入：x = 2.10000, n = 3 输出：9.26100
示例 3：输入：x = 2.00000, n = -2 输出：0.25000
解释：2^-2 = (1/2)^2 = 1/4 = 0.25
提示： -100.0 < x < 100.0  -2^31 <= n <= 2^31-1  -10^4 <= x^n <= 10^4
'''

def myPow(x, n):
    if n < 0:
        neg = True
        n = -n
    else:
        neg = False
    ans, p, step, m = 1.0, [1], [x], 0
    while m < n:
        if m + p[-1] <= n:
            ans *= step[-1]
            step.append(step[-1] * step[-1])
            m += p[-1]
            p.append(p[-1] * 2)
        else:
            step.pop()
            p.pop()
    if neg:
        ans = 1.0 / ans
    return ans
    
print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))

#98.43
#75.28