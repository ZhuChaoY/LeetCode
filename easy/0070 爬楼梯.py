'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
输入： 2 输出： 2  1 阶 + 1 阶、 2 阶
输入： 3 输出： 3  1 阶 + 1 阶 + 1 阶、 1 阶 + 2 阶、 2 阶 + 1 阶
'''

def climbStairs(n):
    if n <= 2:
        return n
    else:
        dic = {0: 1, 1: 2}
        for i in range(2, n):
            dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n - 1]
    
print(climbStairs(3))
print(climbStairs(4))
        
#95.49
#34.96
