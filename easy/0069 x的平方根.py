'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
输入: 4 输出: 2
输入: 8 输出: 2 说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
'''

def mySqrt(x):
    if x == 0:
        return 0
    elif x < 4:
        return 1
    else:
        l, r = 2, x // 2 + 1
        while r - l > 1:
            m = (l + r) // 2
            f_m = m * m
            if f_m < x:
                l = m
            elif f_m > x:
                r = m
            else:
                return m
        return l
    
print(mySqrt(4))
print(mySqrt(9))
print(mySqrt(26))
                
#86.37
#97.14

