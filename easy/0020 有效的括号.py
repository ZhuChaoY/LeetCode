'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()" 输出: true
输入: "()[]{}" 输出: true
输入: "(]" 输出: false
输入: "([)]" 输出: false
输入: "{[]}" 输出: true
'''

def isValid(s):
    dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
    flag = ['?']
    for x in s:
        if x in dic:
            flag.append(x)
        elif x != dic[flag.pop()]:
            return False
    return len(flag) == 1
    
#def isValid(s):
#    while '{}' in s or '()' in s or '[]' in s:
#            s = s.replace('{}', '')
#            s = s.replace('[]', '')
#            s = s.replace('()', '')
#    return s == ''
    
print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))    
print(isValid('{[]}'))

#97.75
#60.30