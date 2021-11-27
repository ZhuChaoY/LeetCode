'''
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
示例 1： 输入：nums = [1,2,2]  输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：输入：nums = [0]  输出：[[],[0]]
提示：1 <= nums.length <= 10  -10 <= nums[i] <= 10
'''

def subsetsWithDup(nums):
    ans = [[]]
    for num in nums:
        tmps = []
        for an in ans:
            tmp = sorted(an + [num]) 
            if tmp not in ans:
                tmps.append(tmp)
        ans += tmps
    return ans

    
print(subsetsWithDup([1, 2, 2]))
print(subsetsWithDup([0]))

#75.39
#65.63