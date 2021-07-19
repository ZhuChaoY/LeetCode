'''
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
输入：28 输出：True 解释：28 = 1 + 2 + 4 + 7 + 14; 1, 2, 4, 7, 和 14。
输入：num = 6 输出：true
输入：num = 496 输出：true
输入：num = 8128 输出：true
输入：num = 2 输出：false
'''

def checkPerfectNumber(num):
    if num < 6:
        return False
    S = 1
    for i in range(2, num):
        if i ** 2 > num:
            break
        if num % i == 0:
            S += (i + num // i)
    return S == num

print(checkPerfectNumber(28))
print(checkPerfectNumber(6))
print(checkPerfectNumber(496))    

#5.71
#5.46