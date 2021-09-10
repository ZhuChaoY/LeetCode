'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
请使用 原地 算法。
进阶：一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
示例 1: 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
       输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
提示： m == matrix.length  n == matrix[0].length  1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
'''

def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    r, c = [], []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i not in r:
                    r.append(i)
                if j not in c:
                    c.append(j)
    for i in range(m):
        if i in r:
            matrix[i] = [0] * n
        else:
            for j in c:
                matrix[i][j] = 0
    return matrix
            
print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))

#87.71
#14.66