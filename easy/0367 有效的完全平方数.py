'''
给定一个正整数num，编写一个函数，如果num是一个完全平方数，则返回 True，否则返回 False。
输入：16 输出：True
输入：14 输出：False
'''

def isPerfectSquare(num):
    if num == 1:
        return True
    l, r = 1, num
    while r - l > 1:
        m = (l + r) // 2
        m_2 = m ** 2
        if m_2 < num:
            l = m
        elif m_2 > num:
            r = m
        else:
            return True
    return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))
        
#73.45
#78.00