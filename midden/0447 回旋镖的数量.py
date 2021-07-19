'''
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离
和 i 和 k 之间的距离相等（需要考虑元组的顺序）。找到所有回旋镖的数量。你可以假设 n 
最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
示例: 输入: [[0,0],[1,0],[2,0]] 输出: 2
解释: 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''

def numberOfBoomerangs(points):
    n, ans = len(points), 0
    dis_dict = [{} for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            dis = (points[i][0] - points[j][0]) ** 2 + \
                  (points[i][1] - points[j][1]) ** 2
            if dis not in dis_dict[i]:
                dis_dict[i][dis] = 1
            else:
                ans += 2 * dis_dict[i][dis]
                dis_dict[i][dis] += 1
            if dis not in dis_dict[j]:
                dis_dict[j][dis] = 1
            else:
                ans += 2 * dis_dict[j][dis]
                dis_dict[j][dis] += 1
    return ans
        
print(numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))    

#97.36
#15.96