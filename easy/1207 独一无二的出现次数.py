'''
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
示例 1：输入：arr = [1,2,2,1,1,3] 输出：true
解释：在该数组中，1 出现了3次，2 出现了2次，3 只出现了 1 次。没有两个数的出现次数相同。
示例 2：输入：arr = [1,2] 输出：false
示例 3：输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]  输出：true
提示：1 <= arr.length <= 1000   -1000 <= arr[i] <= 1000
'''

def uniqueOccurrences(arr):
    count_dict = {}
    for x in arr:
        if x not in count_dict:
            count_dict[x] = 1
        else:
            count_dict[x] += 1
    return len(count_dict) == len(set(count_dict.values()))
    
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

#60.55
#29.49