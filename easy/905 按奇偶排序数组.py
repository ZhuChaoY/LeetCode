'''
给定一个非负整数数组 A，返回一个数组，在该数组中， A的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。
示例：输入：[3,1,2,4] 输出：[2,4,3,1] 
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
提示： 1 <= A.length <= 5000  0 <= A[i] <= 5000
'''

def sortArrayByParity(nums):
    p = 0
    for q in range(len(nums)):
        if nums[q] % 2 == 0:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
    return nums
    
print(sortArrayByParity([3,1,2,4]))

#87.90
#88.72