'''
给你一个仅由数字6和9组成的正整数num。你最多只能翻转一位数字，将6变成9，或者把9变成6。
请返回你可以得到的最大数字。
示例 1：输入：num = 9669 输出：9969 解释：改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。 改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。 其中最大的数字是 9969 。
示例 2：输入：num = 9996 输出：9999 解释：将最后一位从6变到9，其结果9999是最大的数。
示例 3：输入：num = 9999 输出：9999 解释：无需改变就已经是最大的数字了。
提示： 1 <= num <= 10^4 num 每一位上的数字都是 6 或者 9 。
'''

def maximum69Number(num):
    num = list(str(num))
    for i in range(len(num)):
        if num[i] == '6':
            num[i] = '9'
            break
    return int(''.join(num))
        
print(maximum69Number(9669))
print(maximum69Number(9996))
print(maximum69Number(9999))

#99.15
#5.12