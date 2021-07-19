'''
给你两个有序整数数组nums1和nums2，请你将 nums2合并到nums1中，使nums1成为一个有序数组。
初始化nums1和nums2的元素数量分别为 m和n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
输入: nums1 = [1,3,5,7,0,0,0], m = 4; nums2 = [2,4,6], n = 3
输出: [1,2,3,4,5,6,7]
Do not return anything, modify nums1 in-place instead.
'''

def merge(nums1, m, nums2, n):
    temp = nums1[:m]
    p, q = 0, 0
    while p < m and q < n:
        if temp[p] > nums2[q]:
            nums1[p + q] = nums2[q]
            q += 1
        else:
            nums1[p + q] = temp[p]
            p += 1      
    if q == n:
        nums1[(p + n): (m + n)] = temp[p: ]
    elif p == m:
        nums1[(q + m): (m + n)] = nums2[q: ]
        
    return nums1
            
print(merge([1, 3, 5, 7, 0, 0, 0], 4, [2, 4, 6], 3))

#90.39
#61.64
