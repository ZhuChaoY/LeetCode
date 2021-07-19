'''
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
输入: 16 输出: true
输入: 5 输出: false
进阶： 你能不使用循环或者递归来完成本题吗？
'''

def isPowerOfThree(num):
    if num <= 0:
        return False
    while num > 1:
        if num % 4 != 0:
            return False
        else:
            num = num // 4
    return num == 1

print(isPowerOfThree(16))
print(isPowerOfThree(5))

#98.25
#92.54

