'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121 输出: true
输入: -121 输出: false
输入: 10 输出: false
'''

def isPalindrome(x):
    if x < 0:
        return False
    x_reverse = int(str(x)[::-1])
    return x_reverse == x
    
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))

#98.94
#40.36