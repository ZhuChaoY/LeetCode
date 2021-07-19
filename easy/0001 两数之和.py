'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。你可以假设每种输入只会对应一个答案。数组中同一个元素不能使用两遍。
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]
'''

def twoSum(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        num2 = target - num
        if num2 in num_dict:
            return [num_dict[num2], index]
        num_dict[num] = index

print(twoSum([2, 7, 11, 15], 9))

#92.03
#27.34