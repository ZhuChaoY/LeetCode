'''
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
输入: ["flower","flow","flight"] 输出: "fl"
输入: ["dog","racecar","car"] 输出: "" 解释: 输入不存在公共前缀。
所有输入只包含小写字母 a-z 。
'''

def longestCommonPrefix(strs):
    ans = ''
    for x in zip(*strs):
        if len(set(x)) == 1:
            ans += x[0]
        else:
            break  
    return ans
    
'''
zip(*strs) ==> 
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
'''

print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['dog', 'racecar', 'car']))

#100.00
#62.02 

