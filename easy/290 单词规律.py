'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存
在着双向连接的对应规律。
输入: pattern = "abba", str = "dog cat cat dog" 输出: true
输入: pattern = "abba", str = "dog cat cat fish" 输出: false
输入: pattern = "aaaa", str = "dog cat cat dog" 输出: false
输入: pattern = "abba", str = "dog dog dog dog" 输出: false
说明: 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
'''

def wordPattern(pattern, Str):
    x = pattern
    y = Str.split()
    if len(x) != len(y):
        return False
    dict1 = {}
    for i in range(len(x)):
        if x[i] not in dict1:
            dict1[x[i]] = y[i]
        else:
            if dict1[x[i]] != y[i]:
                return False
    dict2 = {}
    for i in range(len(y)):
        if y[i] not in dict2:
            dict2[y[i]] = x[i]
        else:
            if dict2[y[i]] != x[i]:
                return False
    return True            
    
print(wordPattern('abba', 'dog cat cat dog'))
print(wordPattern('abba', 'dog cat cat fish'))   
print(wordPattern('aaaa', 'dog cat cat dog')) 
print(wordPattern('abba', 'dog dog dog dog')) 

#66.69
#67.13