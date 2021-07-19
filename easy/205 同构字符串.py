'''
给定两个字符串 s 和 t，判断它们是否是同构的。 如果 s 中的字符可以被替换得到 t ，
那么这两个字符串是同构的。所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。
两个字符不能映射到同一个字符上，但字符可以映射自己本身。
输入: s = "egg", t = "add" 输出: true
输入: s = "foo", t = "bar" 输出: false
输入: s = "paper", t = "title" 输出: true
'''

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    dic1 = {}
    dic2 = {}
    for i in range(len(s)):
        _s = s[i]
        _t = t[i]
        if _s not in dic1:
            dic1[_s] =_t
        else:
            if dic1[_s] != _t:
                return False
        if _t not in dic2:
            dic2[_t] =_s
        else:
            if dic2[_t] != _s:
                return False
    return True
    
print(isIsomorphic('egg', 'add'))
print(isIsomorphic('foo', 'bar'))
print(isIsomorphic('paper', 'title'))
print(isIsomorphic('ab', 'aa'))

#64.68
#80.00
