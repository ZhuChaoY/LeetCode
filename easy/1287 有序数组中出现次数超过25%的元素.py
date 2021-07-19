'''
给你一个非递减的有序整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总
数的 25%。请你找到并返回这个整数
示例：输入：arr = [1,2,2,6,6,6,6,7,10]  输出：6
提示： 1 <= arr.length <= 10^4   0 <= arr[i] <= 10^5
'''

def findSpecialInteger(arr):
    n = len(arr)
    if n <= 2:
        return arr[0]
    t = n // 4
    ans, k = '', 0
    for x in arr:
        if x == ans:
            k += 1
            if k > t:
                return ans
        else:
            ans = x
            k = 1
    
print(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))

#100
#62.54