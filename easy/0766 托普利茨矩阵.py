'''
给你一个m x n的矩阵matrix。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]] 输出：true
解释： 在上述矩阵中, 其对角线为: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]",
 "[3, 3]", "[4]"。 各条对角线上的所有元素均相同, 因此答案是 True 。
输入：matrix = [[1,2],[2,2]] 输出：false 解释： 对角线 "[1, 2]" 上的元素不同。
提示： m == matrix.length n == matrix[i].length 
1 <= m, n <= 20 0 <= matrix[i][j] <= 99
进阶： 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，
该怎么办？ 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
'''

def isToeplitzMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    if 1 in [m, n]:
        return True
    idx_x = list(range(0, m - 1)) + [0] * (n - 2)
    idx_y = [0] * (m - 1) + list(range(1, n - 1))
    for i, j in zip(idx_x, idx_y):
        v = matrix[i][j]
        for k in range(1, min(m - i, n - j)):
            _v = matrix[i + k][ j + k]
            if _v != v:
                return False
    return True    
    
print(isToeplitzMatrix([[1,2,3,4], [5,1,2,3], [9,5,1,2]]))
print(isToeplitzMatrix([[1,2], [2,2]]))
print(isToeplitzMatrix([[11,74,0,93], [40,11,74,7]]))

#85.68
#81.28