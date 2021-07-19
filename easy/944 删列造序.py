'''
给你由n个小写字母字符串组成的数组 strs，其中每个字符串长度相等。这些字符串可以每个一行，
排成一个网格。例如，strs = ["abc", "bce", "cae"] 可以排列为：abc bce cae
你需要找出并删除不是按字典序升序排列的列。在上面的例子（下标从 0 开始）中，列0（'a',
 'b', 'c'）和列 2（'c', 'e', 'e'）都是按升序排列的，而列 1（'b', 'c', 'a'）不是，
所以要删除列 1 。 返回你需要删除的列数。
示例 1： 输入：strs = ["cba","daf","ghi"]  输出：1 
示例 2：输入：strs = ["a","b"] 输出：0
示例 3：输入：strs = ["zyx","wvu","tsr"] 输出：3  3列都是非升序排列的，所以都要删除。
提示： n == strs.length  1 <= n <= 100 1 <= strs[i].length <= 1000
'''

def minDeletionSize(strs):
    n, m = len(strs), len(strs[0])
    ans = 0
    for j in range(m):
        for i in range(1, n):
            if strs[i][j] < strs[i - 1][j]:
                ans += 1
                break
    return ans
    
print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["a", "b"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))

#56.87
#21.83