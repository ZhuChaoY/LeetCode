'''
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
示例 1:输入: nums = [2,3,1,1,4]  输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:输入: nums = [2,3,0,1,4] 输出: 2
提示: 1 <= nums.length <= 10^4  0 <= nums[i] <= 1000
'''

def jump(nums):
    if sum(nums) == 0:
        return 0
    n = len(nums)
    dis = [0]
    for i in range(n - 1):
        v = nums[n - 2 - i]
        if v == 0:
            dis.append(10000)
        else:
            dis.append(min(dis[-v: ]) + 1)
    return dis[-1]
    
    
print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
print(jump([0]))
print(jump([0, 0]))

#23.64
#13.09