'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i]=[starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
示例 1：输入：intervals = [[1,3],[2,6],[8,10],[15,18]] 
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：输入：intervals = [[1,4],[4,5]]  输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
提示： 1 <= intervals.length <= 10^4 intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''

def merge(intervals):
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
    
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))

#70.30
#37.78