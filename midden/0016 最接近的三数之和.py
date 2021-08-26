'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：输入：nums = [-1,2,1,-4], target = 1 输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
提示： 3 <= nums.length <= 10^3  -10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''

def threeSumClosest(nums, target):
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    X = sorted(set(nums))
    n = len(X)
    m = 10000
    for i in range(n):
        a = X[i]
        if a > (target + m) / 3:
            break
        for j in range(i, n):
            b = X[j]
            if (a + b) > (target + m) * 2 / 3:
                break
            for k in range(j, n):
                c = X[k]
                diff = abs(a + b + c - target)
                if diff < m:
                    tmp = [a, b, c]
                    if tmp.count(a) <= num_dict[a] and \
                        tmp.count(b) <= num_dict[b]:
                            m = diff
                            ans = a + b + c
    return ans

print(threeSumClosest([-1, 2, 1, -4], 2))

#5.04
#16.69