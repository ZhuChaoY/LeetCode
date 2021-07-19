'''
在大小为2N的数组A中有N+1个不同的元素，其中有一个元素重复了N次。返回重复了N次的那个元素。
示例 1： 输入：[1,2,3,3] 输出：3 
示例 2： 输入：[2,1,2,5,3,2] 输出：2
示例 3： 输入：[5,1,5,2,5,3,5,4] 输出：5
提示： 4 <= A.length <= 10000  0 <= A[i] < 10000  A.length 为偶数
'''

def repeatedNTimes(nums): 
    s = []
    for num in nums:
        if num not in s:
            s.append(num)
        else:
            return num
    
print(repeatedNTimes([1,2,3,3]))
print(repeatedNTimes([2,1,2,5,3,2]))
print(repeatedNTimes([5,1,5,2,5,3,5,4]))

#93.33
#50.50