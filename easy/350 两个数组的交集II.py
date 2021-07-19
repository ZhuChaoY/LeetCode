'''
给定两个数组，编写一个函数来计算它们的交集。
输入：nums1 = [1,2,2,1], nums2 = [2,2] 输出：[2,2]
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4] 输出：[4,9]
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 我们可以不考虑
输出结果的顺序。如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？
'''

def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i, j, ans = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
            j += 1
    return ans

print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4])) 
            
#63.69
#28.64

