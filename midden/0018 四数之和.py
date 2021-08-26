'''
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部
条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：
0 <= a, b, c, d < n  a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
示例 1：输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：输入：nums = [2,2,2,2,2], target = 8  输出：[[2,2,2,2]]
提示：1 <= nums.length <= 200 -10^9 <= nums[i] <= 10^9 -10^9 <= target <= 10^9
'''

def fourSum(nums, target):
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    X = sorted(set(nums))
    n = len(X)
    ans = []
    for i in range(n):
        a = X[i]
        if a > target / 4:
            break
        for j in range(i, n):
            b = X[j]
            if a + b > target / 2:
                break
            for k in range(j, n):
                c = X[k]
                d = target - a - b - c
                if d < c:
                    break
                if d in num_dict:
                    tmp = [a, b, c, d]
                    if tmp.count(a) <= num_dict[a] and \
                        tmp.count(b) <= num_dict[b] and \
                        tmp.count(c) <= num_dict[c]:
                            ans.append(tmp)
    return ans
    
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([2, 2, 2, 2, 2], 8))

#69.22
#63.15

