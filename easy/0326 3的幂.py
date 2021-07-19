'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
输入: 27 输出: true
输入: 0 输出: false
输入: 9 输出: true
输入: 45 输出: false
进阶： 你能不使用循环或者递归来完成本题吗？
'''

def isPowerOfThree(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 3 != 0:
            return False
        else:
            n = n // 3
    return n == 1

print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(45))
    
#98.06
#32.08
