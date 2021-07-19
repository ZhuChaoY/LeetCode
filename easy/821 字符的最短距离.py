'''
给你一个字符串s和一个字符c，且c是s中出现过的字符。返回一个整数数组answer，
其中answer.length==s.length且answer[i]是s中从下标i到离它最近的字符c的距离。
两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
示例 1： 输入：s = "loveleetcode", c = "e" 输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 3 。
对于下标4,出现在下标3和下标5处的'e'都离它最近，但距离是一样的abs(4-3)==abs(4-5) = 1。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
示例 2： 输入：s = "aaab", c = "b" 输出：[3,2,1,0]
提示： 1 <= s.length <= 104 s[i] 和 c 均为小写英文字母 
题目数据保证 c 在 s 中至少出现一次
'''

def shortestToChar(s, c):
    f, b, p = [], [], -1
    for i in range(len(s)):
        if s[i] != c:
            if p == -1:
                f.append(105)
            else:
                f.append(i - p)
        else:
            f.append(0)
            b.extend(list(range(i - p))[::-1])
            p = i
    b.extend([105] * (len(s) - p + 1))
    return [min(x, y) for x, y in zip(f, b)]
            
print(shortestToChar('loveleetcode', 'e'))
print(shortestToChar('aaab', 'b'))
print(shortestToChar('abaa', 'b'))
print(shortestToChar('baaa', 'b'))
      
#82.73
#5.50