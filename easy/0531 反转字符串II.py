'''
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进
行反转。如果剩余字符少于 k 个，则将剩余字符全部反转。 如果剩余字符小于 2k 但大于或等于
k 个，则反转前 k 个字符，其余字符保持原样。
输入: s = "abcdefg", k = 2 输出: "bacdfeg" 该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
'''

def reverseStr(s, k):
    n = len(s) 
    p, q = n // (2 * k), n % (2 * k)
    s = list(s)
    for i in range(p):
        s[(2 * i) * k: (2 * i + 1) * k] = s[(2 * i) * k: (2 * i + 1) * k][::-1]
    s[(2 * p * k): (2 * p * k + min(q, k))] = \
        s[(2 * p * k): (2 * p * k + min(q, k))][::-1]
    return ''.join(s)

print(reverseStr('abcdefg', 2))
print(reverseStr('abcd', 2))
print(reverseStr('abcdefg', 1))

#91.13
#7.40
