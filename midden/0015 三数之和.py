'''
给你一个包含n个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：输入：nums = [-1,0,1,2,-1,-4]  输出：[[-1,-1,2],[-1,0,1]]
示例 2： 输入：nums = [] 输出：[]
示例 3： 输入：nums = [0]  输出：[]
提示： 0 <= nums.length <= 3000  -10^5 <= nums[i] <= 10^5
'''

def threeSum(nums):
    if len(nums) < 3:
        return []
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
        if a > 0:
            break
        for j in range(i, n):
            b = X[j]
            c = -a - b
            if c < b:
                break
            if c in num_dict:
                tmp = [a, b, c]
                if tmp.count(a) <= num_dict[a] and \
                    tmp.count(b) <= num_dict[b]:
                        ans.append(tmp)
    return ans
    
                   
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([]))
print(threeSum([0]))
print(threeSum([-2, 1, 1]))

#99.62
#8.72




