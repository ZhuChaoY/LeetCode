'''
给定一个非空且只包含非负数的整数数组nums, 数组的度的定义是指数组里任一元素频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
输入: [1, 2, 2, 3, 1] 输出: 2
输入数组的度是2，因为元素1和2的出现频数最大，均为2.连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
输入: [1,2,2,3,1,4,2] 输出: 6
nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
'''

def findShortestSubArray(nums):
    hash_map = {}
    for index, num in enumerate(nums):
        if num not in hash_map:
            hash_map[num] = [index]
        else:
            hash_map[num].append(index)
    
    max_n = max([len(x) for x in hash_map.values()])
    ans = len(nums)
    for value in hash_map.values():
        if len(value) == max_n:
            ans = min(ans, max(value) - min(value) + 1)
    return ans
    
print(findShortestSubArray([1, 2, 2, 3, 1]))    
print(findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))

#97.37
#5.01