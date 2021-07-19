'''
给你一个长度固定的整数数组arr，请你将该数组中出现的每个零都复写一遍，将其余的元素向右移。
注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组就地进行上述修改，不要从函数返回任何东西。
示例 1：输入：[1,0,2,3,0,4,5,0]  输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：输入：[1,2,3] 输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
提示： 1 <= arr.length <= 10000  0 <= arr[i] <= 9
'''

def duplicateZeros(arr):
    n = len(arr)
    p = 0
    while p < n - 1:
        if arr[p] != 0:
            p += 1
        else:
            arr.pop(-1)
            arr.insert(p + 1, 0)
            p += 2
    return arr
    
    
print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicateZeros([1, 2, 3]))

#100
#81.44