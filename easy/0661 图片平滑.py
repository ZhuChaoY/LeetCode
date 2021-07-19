'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平
均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不
足八个，则尽可能多的利用它们。
输入: [[1,1,1],[1,0,1],[1,1,1]] 输出: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
解释: 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
给定矩阵中的整数范围为 [0, 255]. 矩阵的长和宽的范围均为 [1, 150]。
'''

def imageSmoother(M):
    n, m, ans = len(M), len(M[0]), []
    for i in range(n):
        line = []
        for j in range(m):
            S = []
            for _i in range(max(i - 1, 0), min(i + 2, n)):
                for _j in range(max(j - 1, 0), min(j + 2, m)):
                    S.append(M[_i][_j])                
            line.append(int(sum(S) / len(S)))
        ans.append(line)
    return ans
    
print(imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
print(imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))    
    
#69.18
#21.10