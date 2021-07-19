'''
在一个平衡字符串中,'L'和'R'字符的数量是相同的。给你一个平衡字符串s，请你将它分割成尽可
能多的平衡字符串。注意：分割得到的每个字符串都必须是平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量 。
示例 1：输入：s = "RLRRLLRLRL" 输出：4  解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL"
示例 2：输入：s = "RLLLLRRRLR" 输出：3 解释：s 可以分割为 "RL"、"LLLRRR"、"LR"
示例 3：输入：s = "LLLLRRRR" 输出：1 解释：s 只能保持原样 "LLLLRRRR".
示例 4：输入：s = "RLRRRLLRLL" 输出：2 解释：s 可以分割为 "RL"、"RRRLLRLL".
提示： 1 <= s.length <= 1000  s[i] = 'L' 或 'R'   s 是一个平衡字符串
'''

def balancedStringSplit(s):
    diff, ans = 0, 0
    for x in s:
        if x == 'R':
            diff += 1
        else:
            diff -= 1
        if diff == 0:
            ans += 1
    return ans
        
print(balancedStringSplit('RLRRLLRLRL'))
print(balancedStringSplit('RLLLLRRRLR'))
print(balancedStringSplit('LLLLRRRR'))
print(balancedStringSplit('RLRRRLLRLL'))

#65.86
#83.41