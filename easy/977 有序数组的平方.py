'''
按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100] 排序后，数组变为 [0,1,9,16,100]
示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
提示：  1 <= nums.length <= 104 -104 <= nums[i] <= 104  nums已按非递减顺序排序
进阶： 请你设计时间复杂度为 O(n) 的算法解决本问题
'''

def sortedSquares(nums):
    l, r, ans = 0, len(nums) - 1, []
    while l <= r:
        _l, _r = nums[l] ** 2, nums[r] ** 2
        if _l >= _r:
            ans.append(_l)
            l += 1
        else:
            ans.append(_r)
            r -= 1
    return ans[::-1]
    
print(sortedSquares([-4, -1, 0, 3, 10]))   
print(sortedSquares([-7, -3, 2, 3, 11]))   
print(sortedSquares([-5, -3, -2, -1]))   

#13.15
#8.08