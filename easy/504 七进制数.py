'''
给定一个整数，将其转化为7进制，并以字符串形式输出。
输入: 100 输出: "202"
输入: -7 输出: "-10"
'''

def convertToBase7(num):
    ans = ''
    if num < 0:
        temp = '-'
        num *= -1
    elif num == 0:
        return '0'
    else:
        temp = ''
    while num > 0:
        ans = str(num % 7) + ans
        num //= 7
    return temp + ans

print(convertToBase7(100))
print(convertToBase7(-7))
    
#90.27
#5.76