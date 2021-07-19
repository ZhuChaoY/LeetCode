'''
如果数组是单调递增或单调递减的，那么它是单调的。如果对于所有i<=j，A[i]<=A[j]，那么数
组A是单调递增的。如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。
示例 1： 输入：[1,2,2,3] 输出：true
示例 2： 输入：[6,5,4,4] 输出：true
示例 3： 输入：[1,3,2] 输出：false
示例 4： 输入：[1,2,4,5] 输出：true
示例 5： 输入：[1,1,1] 输出：true
提示： 1 <= A.length <= 50000  -100000 <= A[i] <= 100000
'''

def isMonotonic(nums):
    if len(nums) <= 2:
        return True
    flag = 0
    for i in range(1, len(nums)):
        if flag == 0:
            flag = nums[i] - nums[i - 1]
        else:
            if flag * (nums[i] - nums[i - 1]) < 0:
                return False
    return True
    
print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))
print(isMonotonic([1,2,4,5]))
print(isMonotonic([1,1,1]))

#95.84
#70.89