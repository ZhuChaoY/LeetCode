'''
对于字符串S和T，只有在S = T + ... + T（T自身连接1次或多次）时，我们才认定 “T能除尽S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
示例 1：输入：str1 = "ABCABC", str2 = "ABC"  输出："ABC"
示例 2：输入：str1 = "ABABAB", str2 = "ABAB" 输出："AB"
示例 3：输入：str1 = "LEET", str2 = "CODE" 输出：""
提示：1 <= str1.length <= 1000  1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母
'''

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    else:
        l1, l2 = len(str1), len(str2)
        for i in range(min(l1, l2), 0, -1):
            if l1 % i == 0 and l2 % i == 0:
                return str1[:i]
    
print(gcdOfStrings('ABCABC', 'ABC'))
print(gcdOfStrings('ABABAB', 'ABAB'))
print(gcdOfStrings('LEET', 'CODE'))

#71.60
#36.00