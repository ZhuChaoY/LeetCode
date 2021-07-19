'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
返回的下标值（index1 和 index2）不是从零开始的。 你可以假设每个输入只对应唯一的答案，
而且你不可以重复使用相同的元素。
输入: numbers = [2, 3, 4, 5, 7, 8], target = 8 输出: [2, 4]
'''

def twoSum(numbers, target):
    p, q = 1, len(numbers)
    while True:
        SUM = numbers[p - 1] + numbers[q - 1]
        if SUM == target:
            return [p, q]
        elif SUM > target:
            q -= 1
        else:
            p += 1
                    
print(twoSum([2, 3, 4, 5, 7, 8], 8))        

#77.28
#19.49
