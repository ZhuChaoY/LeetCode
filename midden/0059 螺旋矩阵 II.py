'''
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 
正方形矩阵 matrix 。
示例 1: 输入：n = 3 输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2： 输入：n = 1 输出：[[1]]
提示： 1 <= n <= 20
'''

def generateMatrix(n):
    ans = [[0 for i in range(n)] for j in range(n)]
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))
    k, i, j, num = 0, 0, 0, 1
    while num <= n * n:
        ans[i][j] = num
        num += 1
        d = D[k % 4]
        if not (((k + 3) // 4 <= i + d[0] <= n - 1 - (k + 1) // 4) \
                and ((k // 4 <= j + d[1] <= n - 1 - (k + 2) // 4))):
            k += 1
            d = D[k % 4]
        i += d[0]
        j += d[1]
    return ans
    
print(generateMatrix(3))
print(generateMatrix(1))

#47.62
#44.43