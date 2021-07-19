'''
给定两个数组，编写一个函数来计算它们的交集。
输入：nums1 = [1,2,2,1], nums2 = [2,2] 输出：[2]
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4] 输出：[9,4]
'''

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))    
    
#87.73
#42.18

