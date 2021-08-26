'''
给定两个整数，被除数 dividend和除数divisor。将两数相除，不使用乘法、除法和mod运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，
例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
示例 1:输入: dividend = 10, divisor = 3  输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:输入: dividend = 7, divisor = -3 输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
提示： 被除数和除数均为 32 位有符号整数。  除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
本题中，如果除法结果溢出，则返回 2^31 − 1。
'''

def divide(dividend, divisor):
    if dividend < 0:
        flag1 = False
        dividend = - dividend
    else:
        flag1 = True
    if divisor < 0:
        flag2 = False
        divisor = - divisor
    else:
        flag2 = True
    ans, n, step = 0, 1, divisor
    while dividend >= divisor:
        if dividend >= step:
            ans += n
            dividend -= step
            n += 1
            step += divisor
        else:
            n -= 1
            step -= divisor
    if flag1 != flag2:
        ans = - ans
    if ans < -2147483648 or ans > 2147483647:
        ans = 2147483647
    return ans
    
print(divide(10, 3))
print(divide(7, -3))
print(divide(2147483647, 1))
print(divide(2147483647, 2))

#5.97
#41.06



