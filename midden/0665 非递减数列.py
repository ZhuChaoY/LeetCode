'''
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个
非递减数列。我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，
总满足 nums[i] <= nums[i + 1]。
输入: nums = [4,2,3] 输出: true 解释: 可以通过把第一个4变成1使得它成为一个非递减数列。
输入: nums = [4,2,1] 输出: false 解释: 不能在只改变一个元素的情况下将其变为非递减数列。
1 <= n <= 10 ^ 4    - 10 ^ 5 <= nums[i] <= 10 ^ 5
'''

def checkPossibility(nums):
    n = len(nums)
    if n <= 2:
        return True
    k = 0
    for i in range(1, n - 1):
        if nums[i] < nums[i - 1]:
            k += 1
            if i > 1 and nums[i + 1] < nums[i - 1] and nums[i] < nums[i - 2]:
                return False
    if nums[-1] < nums[-2]:
        k += 1
    return k < 2
    
print(checkPossibility([4, 2, 3]))    
print(checkPossibility([4, 2, 1]))  
print(checkPossibility([3, 4, 2, 3])) 

#83.07
#7.03
