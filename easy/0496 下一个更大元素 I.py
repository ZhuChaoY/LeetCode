'''
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。 nums1 中数字 x 的下一个更大
元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
输入: nums1 = [4,1,2], nums2 = [1,3,4,2]. 输出: [-1,3,-1]
对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
输入: nums1 = [2,4], nums2 = [1,2,3,4]. 输出: [3,-1]
对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1。
nums1和nums2中所有元素是唯一的。 nums1和nums2 的数组大小都不超过1000。
'''

def nextGreaterElement(nums1, nums2):
    ans, temps = {}, []
    for num2 in nums2:
        if num2 in nums1:
            temps.append(num2)
        if temps != []:
            for temp in temps.copy():
                if num2 > temp:
                    ans[temp] = num2
                    temps.remove(temp)
    for temp in temps:
        ans[temp] = -1
    return([ans[x] for x in nums1])
    
    
    
print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement([2, 4], [1, 2, 3, 4]))
    
#39.34   
#5.38   
