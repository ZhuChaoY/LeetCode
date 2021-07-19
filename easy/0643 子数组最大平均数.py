'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
输入: [1,12,-5,-6,50,3], k = 4 输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
1 <= k <= n <= 30,000。 所给数据范围 [-10,000，10,000]。
'''

def findMaxAverage(nums, k):
    ans = [sum(nums[:k])]
    for i in range(len(nums) - k):
        ans += [ans[-1] + nums[k + i] - nums[i]]
    return max(ans) / k
    
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))

#98.66
#5.08
