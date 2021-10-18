'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
示例 1：输入：n = 4, k = 2 输出：
[[2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]]
示例 2：
输入：n = 1, k = 1 输出：[[1]]
提示： 1 <= n <= 20  1 <= k <= n
'''

def combine(n, k):
    def C(x, y):
        if x == y:
            return [[i + 1 for i in range(x)]]
        if y == 1:
            return [[i + 1] for i in range(x)]
        else:
            if x == y + 1:
                X = [[i + 1 for i in range(y)]]
            else:
                X = C(x - 1, y)
            if y == 2:
                Y = [[i + 1] for i in range(x - 1)]
            else:
                Y = C(x - 1, y - 1)
            Y = [i + [x] for i in Y]
            return X + Y 
    return C(n, k)


print(combine(2, 2))    
print(combine(4, 2))
print(combine(6, 3))
print(combine(1, 1))
print(combine(20, 4))


#69.60
#5.04