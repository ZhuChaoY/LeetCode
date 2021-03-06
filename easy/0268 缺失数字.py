'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
输入: [3,0,1] 输出: 2
输入: [9,6,4,2,3,5,7,0,1] 输出: 8
说明: 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''

def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
    
print(missingNumber([3, 0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))    

#91.46
#73.41
