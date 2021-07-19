'''
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
输入: [1,2,3] 输出: 6
输入: [1,2,3,4] 输出: 24
'''

def maximumProduct(nums):
    nums = sorted(nums)
    return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
        
print(maximumProduct([1, 2, 3]))
print(maximumProduct([1, 2, 3, 4]))
print(maximumProduct([-1, -2, 4, 5]))
print(maximumProduct([-1, -2, -6, 4, 5, 3]))
    
#47.35
#19.19   