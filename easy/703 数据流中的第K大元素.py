'''
设计一个找到数据流中第k大元素的类class。注意是排序后的第 k 大元素，不是第k个不同的元素。
请实现 KthLargest 类：
KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 返回当前数据流中第 k 大的元素。
输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
最多调用 add 方法 104 次
题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
'''

class KthLargest():
    def __init__(self, k, nums):
        if len(nums) >= k:
            self.nums = sorted(nums)[::-1][:k]
        else:
            self.nums = nums + [-105]
            
    def add(self, val):
        if val > min(self.nums):
            self.nums.remove(min(self.nums))
            self.nums = self.nums + [val]
        return min(self.nums)
        
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))        
print(obj.add(5)) 
print(obj.add(10)) 
print(obj.add(9)) 
print(obj.add(4)) 
        
#5.86
#92.71       