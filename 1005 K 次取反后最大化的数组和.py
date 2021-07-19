'''
给定一个整数数组A，我们只能用以下方法修改该数组：选择某个索引i并将A[i]替换为-A[i]，总共
重复这个过程K次。我们可以多次选择同一个索引i以这种方式修改数组，返回数组可能的最大和。
示例 1：输入：A = [4,2,3], K = 1 输出：5 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：输入：A=[3,-1,0,2], K=3 输出：6 解释：选择索引 (1,2,2)，然后A变为 [3,1,0,2]。
示例 3：输入A=[2,-3,-1,5,-4], K=2 输出：13 选择索引 (1,4)，然后A变为 [2,3,-1,5,4]。
提示： 1 <= A.length <= 10000  1 <= K <= 10000  -100 <= A[i] <= 100
'''

def largestSumAfterKNegations(nums, k):
    nums = sorted(nums)
    for i in range(k):
        if nums[i] < 0:
            nums[i] *= -1
        else:
            r = k - i 
            if r % 2 == 0:
                return sum(nums)
            else:
                return sum(nums) - 2 * min(nums[i - 1], nums[i])
    return sum(nums)
            
print(largestSumAfterKNegations([4, 2, 3], 1))
print(largestSumAfterKNegations([3, -1, 0, 2], 6))
print(largestSumAfterKNegations([2, -3, -1, 5, -4], 2))

#84.37
#5.11