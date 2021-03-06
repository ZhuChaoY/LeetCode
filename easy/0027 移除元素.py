'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后
数组的新长度。不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

给定 nums = [3,2,2,3], val=3, 函数应该返回新的长度 2, 并且 nums中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且nums中的前五个
元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。不需要考虑数组中超出新长度后面的元素。
'''

def removeElement(nums, val):
    n = len(nums)
    p = 0
    for q in range(n):
        if nums[q] != val:
            nums[p] = nums[q]
            p += 1
    return p
                
print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

#89.00
#68.95
