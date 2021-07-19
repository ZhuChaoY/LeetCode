'''
给定两个字符串 s 和 t，它们只包含小写字母。 字符串 t 由字符串 s 随机重排，然后在随机位
置添加一个字母。请找出在 t 中被添加的字母。
输入： s = "abcd" t = "abcde"
输出： e 解释： 'e' 是那个被添加的字母。
'''

def findTheDifference(s, t):
    return chr(sum(map(ord, t)) - sum(map(ord, s)))

print(findTheDifference('abcd', 'abcde'))
    
#70.19
#16.11