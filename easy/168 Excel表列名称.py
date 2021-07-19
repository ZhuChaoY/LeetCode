'''   
给定一个正整数，返回它在 Excel 表中相对应的列名称。
    1 -> A 0
    2 -> B 1
    3 -> C 2
    ...
    26 -> Z 25
    27 -> AA 26
    28 -> AB 27 
输入: 1 输出: "A"
示例 2: 输入: 28 输出: "AB"
输入: 701 输出: "ZY"
702 'ZZ'
703 'AAA'
'''

def convertToTitle(n):
    str_dict = dict(zip(range(1, 26), [chr(i) for i in range(65, 90)]))
    str_dict[0] = 'Z'
    if n < 26:
        return str_dict[n]
    ans = ''
    while n >= 26:
        res = n % 26
        ans = str_dict[res] + ans
        n //= 26
        if res == 0:
            n -= 1
    if n > 0:
        ans = str_dict[n] + ans
    return ans

print(convertToTitle(2))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(703))
        
#84.38
#70.4