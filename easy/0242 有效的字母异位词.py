'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
输入: s = "anagram", t = "nagaram" 输出: true
输入: s = "rat", t = "car" 输出: false
说明: 你可以假设字符串只包含小写字母。
进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    for x in s:
        if x not in s_dict:
            s_dict[x] = 1
        else:
            s_dict[x] += 1
    t_dict = {}
    for x in t:
        if x not in s_dict:
            return False
        if x not in t_dict:
            t_dict[x] = 1
        else:
            t_dict[x] += 1
    return s_dict == t_dict
    
print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))
    
#42.02
#51.27