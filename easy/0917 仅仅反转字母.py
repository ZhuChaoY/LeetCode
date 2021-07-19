'''
给定字符串S，返回“反转后的”字符串，不是字母的字符都保留在原地，而所有字母的位置发生反转。
示例 1： 输入："ab-cd" 输出："dc-ba"
示例 2： 输入："a-bC-dEf-ghIj" 输出："j-Ih-gfE-dCba"
示例 3： 输入："Test1ng-Leet=code-Q!" 输出："Qedo1ct-eeLg=ntse-T!"
提示： S.length <= 100 33 <= S[i].ASCIIcode <= 122  S 中不包含 \ or "
'''

def reverseOnlyLetters(s):
    if s == '':
        return ''
    s = list(s)
    is_l = lambda i: 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122
    p, q = 0, len(s) - 1
    _p, _q = is_l(p), is_l(q)
    while p < q:
        if _p and _q:
            s[p], s[q] = s[q], s[p]
            p += 1
            _p = is_l(p)
            q -= 1
            _q = is_l(q)
        else:
            if not _p:
                p += 1
                _p = is_l(p)
            if not _q:
                q -= 1
                _q = is_l(q)
    return ''.join(s)
            
print(reverseOnlyLetters(''))
print(reverseOnlyLetters('ab-cd'))
print(reverseOnlyLetters('a-bC-dEf-ghIj'))
print(reverseOnlyLetters('Test1ng-Leet=code-Q!'))

#65.72
#52.75