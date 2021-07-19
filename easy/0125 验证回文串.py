'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
输入: "A man, a plan, a canal: Panama" 输出: true
输入: "race a car" 输出: false
'''

def isPalindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
    
#85.4
#38.56
