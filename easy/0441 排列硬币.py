'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。 
n 是一个非负整数，并且在32位有符号整型的范围内。
n = 5 硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

n = 8  硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.
'''

def arrangeCoins(n):
    k = 1
    while n >= k:
        n -= k
        k += 1
    return k - 1

print(arrangeCoins(0))
print(arrangeCoins(5))
print(arrangeCoins(8))
    
#34.01
#36.46
