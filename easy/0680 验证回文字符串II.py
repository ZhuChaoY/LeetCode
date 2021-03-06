'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
输入: "aba" 输出: True
输入: "abca" 输出: True 解释: 你可以删除c字符。
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''

def validPalindrome(s):
    if s == s[::-1]:
        return True
    p, q = 0, len(s) - 1
    while p < q:
        if s[p] == s[q]:
            p += 1
            q -= 1
        else:
            return s[p + 1: q + 1] == s[p + 1: q + 1][::-1] or \
                   s[p: q] == s[p: q][::-1]

print(validPalindrome('aba'))    
print(validPalindrome('abca')) 

#99.19
#20.99
