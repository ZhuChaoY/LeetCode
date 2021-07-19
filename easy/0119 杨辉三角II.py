'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
输入: 3 输出: [1,3,3,1]
'''

def getRow(rowIndex):
    ans = [1]
    while len(ans) < rowIndex + 1:
        ans = [x + y for x, y in zip([0] + ans, ans + [0])]
    return ans

print(getRow(3))
        
#48.5
#92.23 

