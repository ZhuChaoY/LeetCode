'''
每个非负整数N都有其二进制表示。5可以被表示为二进制"101"，11可以用二进制"1011"表示。
除 N=0外，任何二进制表示中都不含前导零。二进制的反码表示是将每个1改为0且每个0变为1。
例如，二进制数 "101" 的二进制反码为 "010"。 
给你一个十进制数 N，请你返回其二进制表示的反码所对应的十进制整数。
示例 1： 输入：5 输出：2 解释：5 的二进制表示为 "101"，其二进制反码为 "010"。
示例 2： 输入：7 输出：0 解释：7 的二进制表示为 "111"，其二进制反码为 "000"。
示例 3： 输入：10 输出：5 解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"。
提示： 0 <= N < 10^9 
本题与 476：https://leetcode-cn.com/problems/number-complement/ 相同
'''

def bitwiseComplement(n):
    return int(''.join([str(1 - int(x)) for x in bin(n)[2:]]), 2)

print(bitwiseComplement(5))
print(bitwiseComplement(7))
print(bitwiseComplement(10))

#34.81
#5.38