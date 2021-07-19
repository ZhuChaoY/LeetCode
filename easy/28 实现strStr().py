'''
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符
串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
输入: haystack = "hello", needle = "ll" 输出: 2
输入: haystack = "aaaaa", needle = "bba" 输出: -1
对于本题而言，当 needle 是空字符串时我们应当返回 0 。
'''

def strStr(haystack, needle):
    if needle == '':
        return 0
    n = len(haystack)
    m = len(needle)
    if m >= n:
        return (haystack == needle) - 1
    for i in range (n - m + 1):
        if haystack[i: (i + m)] == needle:
            return i
    return -1

print(strStr('hello', 'll'))
print(strStr('aaaaa', 'bba'))
print(strStr('aaaaa', ''))
        
#62.74
#85.26
