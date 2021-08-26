'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1: 输入: s = "abcabcbb"  输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2: 输入: s = "bbbbb"  输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3: 输入: s = "pwwkew"  输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4: 输入: s = ""  输出: 0
提示： 0 <= s.length <= 5 * 10^4   s 由英文字母、数字、符号和空格组成
'''

def lengthOfLongestSubstring(s):
    l = len(s)
    n = len(set(s))
    if n <= 2 or n == l:
        return n
    else:
        ans = 2
        p = 0
        _s = [s[p]]
        while True:
            for q in range(p + 1, min(p + n, l)):
                s_q = s[q]
                if s_q not in _s:
                    _s.append(s_q)
                else:
                    ans = max(ans, len(_s))
                    if ans == n:
                        return n
                    else:
                        idx = _s.index(s_q)
                        _s = _s[idx + 1: ] + [s_q]
                        p = q
                        break
            ans = max(ans, len(_s))
            if q == l - 1:
                return ans
                
            
print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('bwf'))
print(lengthOfLongestSubstring('dvdf'))

#84.29
#30.73


