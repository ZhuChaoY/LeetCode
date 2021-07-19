'''
给定一个整数数组arr，如果它是有效的山脉数组就返回true，否则返回false。
让我们回顾一下，如果A满足下述条件，那么它是一个山脉数组：  arr.length >= 3
在 0 < i < arr.length - 1 条件下，存在 i 使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
示例 1： 输入：arr = [2,1]  输出：false
示例 2： 输入：arr = [3,5,5] 输出：false
示例 3： 输入：arr = [0,3,2,1] 输出：true
提示： 1 <= arr.length <= 104  0 <= arr[i] <= 104
'''

def validMountainArray(arr):
    n = len(arr)
    if n <= 2:
        return False
    flag = 1
    for i in range(1, n):
        if (arr[i] - arr[i - 1]) * flag <= 0:
            if flag == 1 and i != 1: 
                flag = -1
            else:
                return False
    return arr[-1]< arr[-2]

print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))

#100
#5.59