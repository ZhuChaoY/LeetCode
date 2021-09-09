'''
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，
可以合并区间）。
示例 1：输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：输入：intervals = [], newInterval = [5,7]输出：[[5,7]]
示例 4：输入：intervals = [[1,5]], newInterval = [2,3] 输出：[[1,5]]
示例 5：输入：intervals = [[1,5]], newInterval = [2,7]  输出：[[1,7]]
提示： 0 <= intervals.length <= 10^4  intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 10^5
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2  0 <= newInterval[0] <= newInterval[1] <= 105
'''

def insert(intervals, newInterval):
    intervals.append(newInterval)
    if len(intervals) == 1: 
        return intervals
    intervals.sort(key = lambda x: x[0])
    ans = intervals[0: 1]
    for inter in intervals[1: ]:
        tmp = ans[-1]
        if tmp[1] >= inter[0]:
            ans[-1] = [tmp[0], max(tmp[1], inter[1])]
        else:
            ans.append(inter)
    return ans
    
    
print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert([], [5, 7]))
print(insert([[1, 5]], [2, 3]))
print(insert([[1, 5]], [2, 7]))

#90.27
#18.54