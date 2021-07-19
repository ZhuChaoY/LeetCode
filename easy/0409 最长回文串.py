'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意: 假设字符串的长度不会超过 1010。
"abccccdd" 7 解释: 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''

def longestPalindrome(s):
    s_dict = {}
    for x in s:
        if x not in s_dict:
            s_dict[x] = 1
        else:
            s_dict[x] += 1
    
    ans = 0
    for y in s_dict.values():
        ans += (y - y % 2)
    return ans + (ans != len(s))

print(longestPalindrome('abccccdd'))
    
#83.28    
#21.45