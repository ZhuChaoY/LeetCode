'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），
而 s 是个短字符串（长度 <=100）。字符串的一个子序列是原始字符串删除一些（也可以不删除）
字符而不改变剩余字符相对位置形成的新字符串。如"ace"是"abcde"的一个子序列而"aec"不是）。
s = "abc", t = "ahbgdc" 返回 true.
s = "axc", t = "ahbgdc" 返回 false.
'''

def isSubsequence(s, t):
    if s == '':
        return True
    i = 0 
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
            if i == len(s):
                return True
    return False

print(isSubsequence('abc', 'ahbgdc'))
print(isSubsequence('axc', 'ahbgdc'))    

#99.65
#53.32