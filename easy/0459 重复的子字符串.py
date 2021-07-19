'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写
英文字母，并且长度不超过10000。
输入: "abab" 输出: True 解释: 可由子字符串 "ab" 重复两次构成。
输入: "aba" 输出: False
输入: "abcabcabcabc"  输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
'''

def repeatedSubstringPattern(s):
    return s in (s + s)[1: -1]

#    n = len(s)
#    if n < 1:
#        return False
#    for i in range(1, n // 2 + 1):
#        if n % i != 0:
#            continue
#        if s[:i] * (n // i) == s:
#            return True
#    return False
    
print(repeatedSubstringPattern('bb'))     
print(repeatedSubstringPattern('abab'))
print(repeatedSubstringPattern('aba'))    
print(repeatedSubstringPattern('abcabcabcabc'))
    
#62.16
#30.51   