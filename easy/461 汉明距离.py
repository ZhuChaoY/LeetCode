'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。注意： 0 ≤ x, y < 231.
输入: x = 1, y = 4 输出: 2 解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
'''

def hammingDistance(x, y):
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    x_len = len(x_bin)
    y_len = len(y_bin)
    if x_len < y_len:
        x_bin = '0' * (y_len - x_len) + x_bin
    elif x_len > y_len:
        y_bin = '0' * (x_len - y_len) + y_bin
    ans = 0
    for i in range(len(x_bin)):
        if x_bin[i] != y_bin[i]:
            ans += 1
    return ans

#    return bin(x ^ y).count('1')
    
#43.68
#47.35