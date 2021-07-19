'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12] 输出: [1,3,12,0,0]
必须在原数组上操作，不能拷贝额外的数组。尽量减少操作次数。
'''

def moveZeroes(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] == 0:
            p = [i]
            for q in range(i + 1, n):
                if nums[q] != 0:
                    nums[p.pop(0)] = nums[q]
                p.append(q)
            for x in p:
                nums[x] = 0                                
            return nums
        
print(moveZeroes([0, 0, 1]))
print(moveZeroes([0, 1, 0, 3, 12]))
print(moveZeroes([0, 2, 0, 4, 5, 0, 12]))
    
#14.41     
#54.53