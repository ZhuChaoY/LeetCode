'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例 1: 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]  输出：[1,2,3,6,9,8,7,4,5]
示例 2： 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
提示： m == matrix.length  n == matrix[i].length
1 <= m, n <= 10  -100 <= matrix[i][j] <= 100
'''

def spiralOrder(matrix):
    n, m = len(matrix), len(matrix[0])
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ans, k, i, j = [], 0, 0, 0
    while len(ans) < n * m:
        ans.append(matrix[i][j])
        d = D[k % 4]
        if not (((k + 3) // 4 <= i + d[0] <= n - 1 - (k + 1) // 4) \
                and ((k // 4 <= j + d[1] <= m - 1 - (k + 2) // 4))):
            k += 1
            d = D[k % 4]
        i += d[0]
        j += d[1]
    return ans
    
print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

#89.40
#74.37