'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
输入: nums = [1,2,3,1], k = 3 输出: true
输入: nums = [1,0,1,1], k = 1 输出: true
输入: nums = [1,2,3,1,2,3], k = 2 输出: false
'''

def containsNearbyDuplicate(nums, k):
    num_dict = {}
    for index, num in enumerate(nums):
        if num not in num_dict or index - num_dict[num] > k:
            num_dict[num] = index
        else:
            return True
    return False
    
print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))   
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))         
            
#89.26
#55.67
