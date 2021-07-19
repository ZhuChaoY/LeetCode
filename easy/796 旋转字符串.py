'''
给定两个字符串, A 和 B。A的旋转操作就是将A最左边的字符移动到最右边。例如, 若A='abcde'，
在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
示例 1: 输入: A = 'abcde', B = 'cdeab' 输出: true
示例 2: 输入: A = 'abcde', B = 'abced' 输出: false
注意： A 和 B 长度不超过 100。
'''

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in s + s[:-1]
    
print(rotateString('abcde', 'cdeab'))
print(rotateString('abcde', 'cbced'))
    
#63.53
#5.37