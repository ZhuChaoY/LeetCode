'''
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
s = s1 + s2 + ... + sn t = t1 + t2 + ... + tm  |n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。
示例 1：输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"  输出：true
示例 2：输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" 输出：false
示例 3： 输入：s1 = "", s2 = "", s3 = ""  输出：true
提示：0 <= s1.length, s2.length <= 100  0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
'''

def isInterleave(s1, s2, s3):
    n, m, k = len(s1), len(s2), len(s3)
    if n + m != k:
        return False
    if n * m == 0:
        return s3 == (s1 + s2)
    res = [(s1, s2)]
    for i in range(k - 1):
        if res == []:
            return False
        s = s3[i]
        new_res = []
        for x, y in res:         
            if s == x[0]:
                if len(x) == 1:
                    if y == s3[(i + 1): ]:
                        return True
                else:
                    tmp = [x[1: ], y]
                    if tmp not in new_res:
                        new_res.append(tmp)
            if s == y[0]:
                if len(y) == 1:
                    if x == s3[(i + 1): ]:
                        return True
                else:
                    tmp = [x, y[1: ]]
                    if tmp not in new_res:
                        new_res.append(tmp)
        res = new_res
        
            
print(isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
print(isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
print(isInterleave('', '', ''))
print(isInterleave('', 'b', 'b'))
print(isInterleave('', 'ab', 'ab'))

#83.48
#96.14


