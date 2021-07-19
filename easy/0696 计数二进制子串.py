'''
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的
所有0和所有1都是组合在一起的。重复出现的子串要计算它们出现的次数。
输入: "00110011" 输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
请注意，一些重复出现的子串要计算它们出现的次数。 另外，“00110011”不是有效的子串，因为
所有的0（和1）没有组合在一起。
输入: "10101" 输出: 4 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量
的连续1和0。
s.length 在1到50,000之间。 s 只包含“0”或“1”字符。
'''

def countBinarySubstrings(s):
    if len(s) == 1:
        return 0
    temp, lens = s[0], [0, 1]
    for x in s[1:]:
        if x == temp:
            lens[-1] += 1
        else:
            temp = x
            lens.append(1)
    ans = 0
    for i in range(1, len(lens)):
        ans += min(lens[i], lens[i - 1])
    return ans

print(countBinarySubstrings('00110011'))
print(countBinarySubstrings('10101'))  
print(countBinarySubstrings('00110'))  
print(countBinarySubstrings('11111'))

#86.58
#5.48