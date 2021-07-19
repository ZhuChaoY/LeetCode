'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
输入: 1 输出: true 解释: 2^0 = 1
输入: 16 输出: true 解释: 2^4 = 16
输入: 218 输出: false
'''

def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 == 1:
            return False
        else:
            n = n // 2
    return n == 1

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(218))
          
#84.57
#45.14