'''
平面上有n个点，点的位置用整数坐标表示points[i]=[xi, yi]。请你计算访问所有这些点需要的
最小时间（以秒为单位）。需要按照下面的规则在平面上移动： 每一秒内，你可以：沿水平方向移
动一个单位长度，或者  沿竖直方向移动一个单位长度，或者跨过对角线移动sqrt(2)个单位长度
（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。必须按照数组中出现的顺序来访问这
些点。在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。
示例 1: 输入：points = [[1,1],[3,4],[-1,0]] 输出：7 解释：一条最佳的访问路径是：
 [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒  从 [3,4] 到 [-1,0] 需要 4 秒  一共需要 7 秒
示例 2： 输入：points = [[3,2],[-2,2]]  输出：5
提示： points.length == n  1 <= n <= 100  points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
'''

def minTimeToVisitAllPoints(points):
    n = len(points)
    if n == 1:
        return 0
    ans = 0
    for i in range(1, n):
        p0, p1 = points[i - 1], points[i]
        ans += max(abs(p0[0] - p1[0]), abs(p0[1] - p1[1]))
    return ans
        
print(minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
print(minTimeToVisitAllPoints([[3, 2], [-2, 2]]))

#94.13
#5.67