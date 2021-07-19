'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。 
示例: 输入：[4,2,5,7] 输出：[4,5,2,7]; [4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
提示：2 <= A.length <= 20000  A.length % 2 == 0 0 <= A[i] <= 1000
'''

def sortArrayByParityII(nums):
    ans = [0] * len(nums)
    p, q = 0, 1
    for num in nums:
        if num % 2 == 0:
            ans[p] = num
            p += 2
        else:
            ans[q] = num
            q += 2
    return ans
    
print(sortArrayByParityII([4, 2, 5, 7]))
print(sortArrayByParityII([2, 0, 3, 4, 1, 3]))

#75.73
#19.51