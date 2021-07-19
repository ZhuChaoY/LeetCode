'''
给定由若干0和1组成的数组A。我们定义N_i：从A[0]到A[i]的第i个子数组被解释为一个二进制数
（从最高有效位到最低有效位）。返回布尔值列表answer，只有当N_i可以被5整除时，
答案answer[i]为true，否则为 false。
示例 1：输入：[0,1,1] 输出：[true,false,false] 解释： 输入数字为 0, 01, 011；也就
是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
示例 2：输入：[1,1,1] 输出：[false,false,false]
示例 3：输入：[0,1,1,1,1,1] 输出：[true,false,false,false,true,false]
示例 4： 输入：[1,1,1,0,1]  输出：[false,false,false,false,false]
提示： 1 <= A.length <= 30000   A[i] 为 0 或 1
'''

def prefixesDivBy5(nums):
    ans = []
    s = 0
    for num in nums:
        s = 2 * s + num
        if s % 5 == 0:
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(prefixesDivBy5([0, 1, 1]))
print(prefixesDivBy5([1, 1, 1]))
print(prefixesDivBy5([0, 1, 1, 1, 1, 1]))
print(prefixesDivBy5([1, 1, 1, 0, 1]))

#59.93
#67.28