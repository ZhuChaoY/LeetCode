'''
给你一个整数数组arr，只有可以将其划分为三个和相等的非空部分时才返回true，否则返回false。
形式上，如果可以找出索引i+1<j且满足(arr[0]+arr[1]+...+arr[i]==arr[i+1]+arr[i+2] +
...+arr[j-1] == arr[j]+arr[j + 1]+...+ arr[arr.length - 1]) 就可以将数组三等分.
示例 1： 输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1] 输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2： 输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1] 输出：false
示例 3： 输入：arr = [3,3,6,5,-2,2,5,1,-9,4] 输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
提示： 3 <= arr.length <= 5 * 10^4   -10^4 <= arr[i] <= 10^4
'''

def canThreePartsEqualSum(arr):
    S = sum(arr)
    if S % 3 != 0:
        return False
    s, k = 0, 0
    for x in arr[:-1]:
        s += x
        if s * 3 == S:
            k += 1
            s = 0
        if k == 2:
            return True
    return False
    
print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))

#60.84
#5.17
    