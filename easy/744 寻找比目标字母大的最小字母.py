'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
输入: letters = ["c", "f", "j"] target = "a" 输出: "c"
输入: letters = ["c", "f", "j"] target = "c" 输出: "f"
输入: letters = ["c", "f", "j"] target = "d" 输出: "f"
输入: letters = ["c", "f", "j"] target = "g" 输出: "j"
输入: letters = ["c", "f", "j"] target = "j" 输出: "c"
输入: letters = ["c", "f", "j"] target = "k" 输出: "c"
letters长度范围在[2, 10000]区间内。 letters 仅由小写字母组成，最少包含两个不同的字母。
目标字母target 是一个小写字母。
'''

def nextGreatestLetter(letters, target):
    if letters[0] > target or letters[-1] <= target:
        return letters[0]
    n = len(letters)
    l, r = 0, n - 1
    while l < r - 1:
        m = (l + r) // 2
        if letters[m] > target:
            r = m
        elif letters[m] <= target:
            l = m
    return letters[l + 1]
        
print(nextGreatestLetter(['c', 'f', 'j'], 'a'))    
print(nextGreatestLetter(['c', 'f', 'j'], 'c'))    
print(nextGreatestLetter(['c', 'f', 'j'], 'd'))
print(nextGreatestLetter(['c', 'f', 'j'], 'g'))
print(nextGreatestLetter(['c', 'f', 'j'], 'j'))
print(nextGreatestLetter(['c', 'f', 'j'], 'k'))
print(nextGreatestLetter(['e', 'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 'n'],
                         'e'))
    
#87.75    
#5.17
