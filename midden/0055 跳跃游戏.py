'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
示例 1： 输入：nums = [2,3,1,1,4]  输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2： 输入：nums = [3,2,1,0,4] 输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 
所以永远不可能到达最后一个下标。
提示：1 <= nums.length <= 3 * 10^4  0 <= nums[i] <= 10^5
'''

def canJump(nums):
    n = len(nums)
    if n == 1:
        return True
    p = n - 2
    while p > 0: 
        if nums[p] == 0:
            flag = True 
            for q in range(1, p + 1):
                if nums[p - q] > q:
                    p = p - q - 1
                    flag = False
                    break
            if flag:
                return False
        else:
            p -= 1
    return nums[0] != 0
                    
print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([0]))
print(canJump([0, 0]))
print(canJump([1, 1]))
print(canJump([2, 0, 0]))
print(canJump([1, 1, 1]))

#92.30
#51.29