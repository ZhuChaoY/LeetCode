'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
输入: [1,3,2,2,5,2,3,7] 输出: 5 原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
'''

def findLHS(nums):
    num_list = sorted(list(set(nums)))
    if len(num_list) <= 1:
        return 0
    count_dict = {}
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    ans = 0            
    for i in range(len(num_list) - 1):
        if num_list[i + 1] - num_list[i] == 1:
            ans = max(ans, count_dict[num_list[i]] + \
                           count_dict[num_list[i + 1]])
    return ans

print(findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
        
#90.46
#55.28
