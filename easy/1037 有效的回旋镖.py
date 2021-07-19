'''
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。给出平面上三个点组成的列表，
判断这些点是否可以构成回旋镖。
示例 1： 输入：[[1,1],[2,3],[3,2]]  输出：true
示例 2： 输入：[[1,1],[2,2],[3,3]]  输出：false
提示：  points.length == 3  points[i].length == 2  0 <= points[i][j] <= 100
'''

def isBoomerang(points):
    a, b, c = points
    return a[0] * (b[1]- c[1]) + b[0] * (c[1]- a[1]) + \
                           c[0] * (a[1]- b[1]) != 0
    
print(isBoomerang([[1, 1], [2, 3], [3, 2]]))
print(isBoomerang([[1, 1], [2, 2], [3, 3]]))

#94.39
#6.63