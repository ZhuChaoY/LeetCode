'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。    
在杨辉三角中，每个数是它左上方和右上方的数的和。
输入: 5 输出:
     [[1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]]
'''

def generate(numRows):
    if numRows == 0:
        return []
    ans = [[1]]
    while len(ans) < numRows:
        ans.append([x + y for x, y in zip([0] + ans[-1], ans[-1] + [0])])
    return ans
    
print(generate(5))
        
#85.43
#52.06 