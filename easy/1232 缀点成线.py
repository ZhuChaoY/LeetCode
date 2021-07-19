'''
在一个 XY坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，coordinates[i]
 = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
示例 1： 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]  输出：true
示例 2： 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] 输出：false
提示： 2 <= coordinates.length <= 1000   coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4 coordinates 中不含重复的点
'''

def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    cal_k = lambda x, y: 'inf' if y[0] - x[0] == 0 \
                               else (y[1] - x[1]) / (y[0] - x[0])
    x0 = coordinates[0]
    k0 = cal_k(coordinates[1], x0) 
    for x in coordinates[2: ]:
        if cal_k(x, x0) != k0:
            return False
    return True
    
print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))

#100
#62.13