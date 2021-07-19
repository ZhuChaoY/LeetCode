'''
给你一个n*n的网格 grid，上面放置着一些1x1x1的正方体。每个值v=grid[i][j]表示v个正方体
叠放在对应单元格 (i, j) 上。放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成
一些不规则三维形体。返回最终这些形体的总表面积。注意：每个形体的底面也需要计入表面积中。
示例 1： 输入：grid = [[2]] 输出：10
示例 2：输入：grid = [[1,2],[3,4]] 输出：34
示例 3：输入：grid = [[1,0],[0,2]] 输出：16
示例 4: 输入：grid = [[1,1,1],[1,0,1],[1,1,1]] 输出：32
示例 5: 输入：grid = [[2,2,2],[2,1,2],[2,2,2]] 输出：46
提示： n == grid.length n == grid[i].length 1 <= n <= 50 0 <= grid[i][j] <= 50
'''

def surfaceArea(grid):
    ans, n = 0, len(grid)
    grid = [[0] * (n + 2)] + [[0] + x + [0] for x in grid] + [[0] * (n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            v = grid[i][j] 
            if v != 0:
                ans += \
                    max(0, v - grid[i - 1][j]) + max(0, v - grid[i][j + 1]) + \
                    max(0, v - grid[i + 1][j]) + max(0, v - grid[i][j - 1]) + 2
    return ans
                
print(surfaceArea([[2]]))
print(surfaceArea([[1,2], [3,4]]))
print(surfaceArea([[1,0], [0,2]]))
print(surfaceArea([[1,1,1],[1,0,1], [1,1,1]]))
print(surfaceArea([[2,2,2], [2,1,2], [2,2,2]]))

#76.67
#17.62