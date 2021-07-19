'''
给你两个二进制字符串，返回它们的和（用二进制表示）。 输入为非空字符串且只包含数字 1和0。
输入: a = "11", b = "1" 输出: "100"
输入: a = "1010", b = "1011" 输出: "10101"
每个字符串仅由字符 '0' 或 '1' 组成。 1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
'''

def addBinary(a, b):
    n_a, n_b = len(a), len(b)
    if n_a < n_b:
        a = '0' * (n_b - n_a) + a
    if n_a > n_b:
        b = '0' * (n_a - n_b) + b
    ans, flag = '', 0
    for i in range(len(a) - 1, -1, -1):
        tmp = int(a[i]) + int(b[i]) + flag
        ans += str(tmp % 2)
        flag = tmp // 2
    if flag == 1:
        ans += '1'
    return ans[::-1]

print(addBinary('11', '1'))
print(addBinary('1010', '1011'))

#38.01
#76.79