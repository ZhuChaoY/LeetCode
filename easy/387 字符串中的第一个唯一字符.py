'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
s = "leetcode" 返回 0
s = "loveleetcode" 返回 2
'''

def firstUniqChar(s):
    str_dict = {}
    for x in s:
        if x not in str_dict:
            str_dict[x] = 1
        else:
            str_dict[x] += 1
    for i in range(len(s)):
        if str_dict[s[i]] == 1:
            return i
    return -1

print(firstUniqChar(''))
print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))        
    
#52.69
#79.39