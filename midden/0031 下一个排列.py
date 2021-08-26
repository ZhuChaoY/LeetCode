'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的
排列（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
示例 1：输入：nums = [1,2,3]  输出：[1,3,2]
示例 2：输入：nums = [3,2,1]  输出：[1,2,3]
示例 3：输入：nums = [1,1,5]  输出：[1,5,1]
示例 4：输入：nums = [1]  输出：[1]
提示： 1 <= nums.length <= 100   0 <= nums[i] <= 100
'''

def nextPermutation(nums):
    p = len(nums) - 1
    while p > 0:
        if nums[p] > nums[p - 1]:
            tmp = nums[p - 1: ]
            S = sorted(set(tmp))
            head = S[S.index(tmp[0]) + 1]
            nums[p - 1] = head
            tmp.remove(head)
            nums[p: ] = sorted(tmp)
            break
        p -= 1
    if p == 0:
        nums[:] = nums[::-1]
    return nums
                    
print(nextPermutation([1, 2, 3]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([1, 1, 5]))
print(nextPermutation([1]))

#78.04
#33.37