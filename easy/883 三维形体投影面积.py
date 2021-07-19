'''
在N*N的网格中，我们放置了一些与x，y，z三轴对齐的1*1*1立方体。每个值v=grid[i][j]表示v
个正方体叠放在单元格 (i, j) 上。现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
投影就像影子，将三维形体映射到二维平面上。从顶部、前面和侧面看立方体，我们会看到“影子”。
返回所有三个投影的总面积。
示例 1： 输入：[[2]] 输出：5 
示例 2： 输入：[[1,2],[3,4]] 输出：17 
示例 3： 输入：[[1,0],[0,2]] 输出：8
示例 4： 输入：[[1,1,1],[1,0,1],[1,1,1]] 输出：14
示例 5： 输入：[[2,2,2],[2,1,2],[2,2,2]] 输出：21
提示： 1 <= grid.length = grid[0].length <= 50 0 <= grid[i][j] <= 50
'''

def projectionArea(grid):
    n, m = len(grid), len(grid[0])
    _x, _y, z = [0] * m, [], 0
    for i in range(n):
        _y.append(max(grid[i]))
        for j in range(m):
            v = grid[i][j]
            _x[j] = max(_x[j], v)
            if v != 0:
                z += 1
    return sum(_x) + sum(_y) + z
    
print(projectionArea([[2]]))
print(projectionArea([[1,2], [3,4]]))
print(projectionArea([[1,0], [0,2]]))
print(projectionArea([[1,1,1], [1,0,1], [1,1,1]]))
print(projectionArea([[2,2,2], [2,1,2], [2,2,2]]))

#56.44
#19.31