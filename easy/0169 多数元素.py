'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入: [3,2,3] 输出: 3
输入: [2,2,1,1,1,2,2] 输出: 2
'''

#摩尔投票法
def majorityElement(nums):
    count = 0
    for num in nums:
        if count == 0:
            ans = num
            count = 1
            continue
        if num == ans:
            count += 1
        else:
            count -= 1
    return ans
            
print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
            
#69.19
#65.98   
