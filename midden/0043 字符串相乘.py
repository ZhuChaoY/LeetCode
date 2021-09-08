'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
它们的乘积也表示为字符串形式。
示例 1:输入: num1 = "2", num2 = "3" 输出: "6"
示例 2: 输入: num1 = "123", num2 = "456" 输出: "56088"
说明： num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''

def multiply(num1, num2):
    if '0' in [num1, num2]:
        return '0'
    l1, l2 = len(num1), len(num2)
    sum_list = [[] for k in range(l1 + l2)]
    for i in range(l1):
        v1 = ord(num1[- i - 1]) - 48
        for j in range(l2):
            v2 = ord(num2[- j - 1]) - 48
            v = v1 * v2
            sum_list[i + j].append(v % 10)
            sum_list[i + j + 1].append(v // 10)
    ans = []
    for k in range(l1 + l2 - 1):
        s = sum(sum_list[k])
        ans.append(str(s % 10))
        sum_list[k + 1].append(s // 10)
    s = sum(sum_list[-1])
    if s != 0:
        ans.append(str(s))
    return ''.join(ans[::-1])
    

print(multiply('2', '3'))
print(multiply('123', '456'))
print(multiply('999', '999'))

#58.02
#5.00
