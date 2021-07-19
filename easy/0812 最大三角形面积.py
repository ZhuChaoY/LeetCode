'''
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
示例: 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]] 输出: 2
解释:  这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
注意: 3 <= points.length <= 50. 不存在重复的点。-50 <= points[i][j] <= 50.
结果误差值在 10^-6 以内都认为是正确答案。
'''

def largestTriangleArea(points):
    area = lambda x1, y1, x2, y2, x3, y3: abs(x1 * (y2 - y3) + \
                                          x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    n, ans = len(points), 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                s = area(points[i][0], points[i][1], points[j][0],
                         points[j][1], points[k][0], points[k][1])
                ans = max(ans, s)
    return ans

print(largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))

#61.81
#39.20