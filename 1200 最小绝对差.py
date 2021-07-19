'''
整数数组arr每个元素都不相同。请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
示例 1： 输入：arr = [4,2,1,3]  输出：[[1,2],[2,3],[3,4]]
示例 2： 输入：arr = [1,3,6,10,15]  输出：[[1,3]]
示例 3： 输入：arr = [3,8,-10,23,19,-4,-14,27]  输出：[[-14,-10],[19,23],[23,27]]
提示： 2 <= arr.length <= 10^5  -10^6 <= arr[i] <= 10^6
'''

def minimumAbsDifference(arr):
    arr = sorted(arr)
    M = 10000000
    for i in range(len(arr) - 1):
        x, y = arr[i], arr[i + 1]
        diff = y - x
        if diff < M:                
            ans = [[x, y]]
            M = diff
        elif diff == M:
            ans.append([x, y])
    return ans
            
print(minimumAbsDifference([4, 2, 1, 3]))
print(minimumAbsDifference([1, 3, 6, 10, 15]))
print(minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))

#100
#94.03