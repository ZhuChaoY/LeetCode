'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
输入: 5 输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
输入: 1 输出: 0 
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
给定的整数保证在 32 位带符号整数的范围内。你可以假定二进制数不包含前导零位。
'''

def findComplement(num):
    return int(''.join([str(1 - int(x)) for x in bin(num)[2:]]), 2)

print(findComplement(5))
print(findComplement(1))

#43.07
#92.99