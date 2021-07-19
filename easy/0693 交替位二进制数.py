'''
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相
邻两位的数字永不相同。
输入：n = 5 输出：true 解释：5 的二进制表示是：101
输入：n = 7 输出：false 解释：7 的二进制表示是：111.
输入：n = 11 输出：false 解释：11 的二进制表示是：1011.
输入：n = 10 输出：true 解释：10 的二进制表示是：1010.
输入：n = 3 输出：false
1 <= n <= 2^31 - 1
'''

def hasAlternatingBits(n):
    return bin(n).replace('00', '').replace('11', '') == bin(n)

print(hasAlternatingBits(5))
print(hasAlternatingBits(7))    
print(hasAlternatingBits(11))
print(hasAlternatingBits(10))
print(hasAlternatingBits(3))

#69.63
#5.63