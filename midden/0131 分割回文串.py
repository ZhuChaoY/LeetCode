'''
给你一个字符串 s，请你将s分割成一些子串，使每个子串都是回文串。返回s所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
示例 1：输入：s = "aab" 输出：[["a","a","b"],["aa","b"]]
示例 2：输入：s = "a"  输出：[["a"]]
提示：1 <= s.length <= 16  s 仅由小写英文字母组成
'''

def partition(s):
    if len(set(s)) == 1:
        x = s[0]
        ans = [[x]]
        for i in range(len(s) - 1):
            new_ans = []
            for a in ans:
                new_ans.extend([a + [x], a[:-1] + [a[-1] + x]])
            ans = new_ans
    else:
        ans = [[s[0]]]
        for x in s[1: ]:
            new_ans = []
            y = ''.join(ans[0] + [x])
            if y == y[::-1]:
                new_ans.append([y])
            for a in ans:
                new_ans.append(a + [x])
                for i in range(len(a) - 1):
                    if a[i + 1] == x:
                        y = ''.join(a[(i + 2): ])
                        if y == y[::-1]:
                            tmp = a[: (i + 1)] + [x + y + x]
                            if tmp not in new_ans:
                                new_ans.append(tmp)
            ans = new_ans
    return ans
    
print(partition('a'))
print(partition('aab'))
print(partition('abba'))
print(partition('abccba'))
print(partition('cbbbcc'))
print(partition('bbbbbb'))

#96.82
#80.43
