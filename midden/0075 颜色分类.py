'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
示例 1：输入：nums = [2,0,2,1,1,0]  输出：[0,0,1,1,2,2]
示例 2：输入：nums = [2,0,1] 输出：[0,1,2]
示例 3：输入：nums = [0] 输出：[0]
示例 4：输入：nums = [1] 输出：[1]
提示： n == nums.length  1 <= n <= 300   nums[i] 为 0、1 或 2
进阶：你可以不使用代码库中的排序函数来解决这道题吗？
     你能想出一个仅使用常数空间的一趟扫描算法吗？
'''

def sortColors(nums):
    n = len(nums)
    if n == 1:
        return nums
    p = 0
    while p < n:
        if nums[p] == 0:
            p += 1
        else:
            break
    q = n - 1
    while q >= 0:
        if nums[q] == 2:
            q -= 1
        else:
            break
    if p >= q:
        return nums
    k = p
    while True:
        if nums[k] == 0:
            if k != p:
                nums[p], nums[k] = 0, nums[p]
            else:
                k += 1
            p += 1
        elif nums[k] == 2:
            nums[k], nums[q] = nums[q], 2
            q -= 1
        else:
            k += 1
        if k == q and nums[k] >= nums[p]:
            break
    return nums
    
print(sortColors([2, 0, 2, 1, 1, 0]))
print(sortColors([1, 2, 0, 2, 0, 0, 1, 1, 0, 1]))
print(sortColors([1, 2, 0]))
print(sortColors([2, 0, 1]))
print(sortColors([0]))
print(sortColors([0, 0]))
print(sortColors([0, 1]))
print(sortColors([1]))

#87.75
#70.74

