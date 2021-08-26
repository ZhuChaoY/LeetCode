'''
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：输入：s = "babad"  输出："bab"  解释："aba" 同样是符合题意的答案。
示例 2：输入：s = "cbbd" 输出："bb"
示例 3： 输入：s = "a" 输出："a"
示例 4：输入：s = "ac" 输出："a"
提示: 1 <= s.length <= 1000   s 仅由数字和英文字母（大写和/或小写）组成
'''

def longestPalindrome(s):
    s_dict = {}
    for (idx, x) in enumerate(s):
        if x not in s_dict:
            s_dict[x] = [idx]
        else:
            s_dict[x].append(idx)
    m = 1
    ans = s[0]
    for idxes in s_dict.values():
        n_idx = len(idxes)
        if n_idx > 1:
            for i in range(n_idx):
                idx1 = idxes[i]
                for j in range(i + 1, n_idx):
                    idx2 = idxes[j]
                    if (idx2 - idx1) > (m  - 1):
                        _s = s[idx1: idx2 + 1]
                        if _s == _s[::-1]:
                            m = len(_s)
                            ans = _s
    return ans         
                

print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))
print(longestPalindrome('a'))
print(longestPalindrome('ac'))

#75.60
#74.68