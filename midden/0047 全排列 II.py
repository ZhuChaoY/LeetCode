'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例 1：输入：nums = [1,1,2]
输出：[[1,1,2], [1,2,1], [2,1,1]]
示例 2：输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
提示：1 <= nums.length <= 8  -10 <= nums[i] <= 10
'''

def permuteUnique(nums):
    def backtrack(X):
        if len(X) >= 2:
            Y = [] 
            for x in set(X):
                _X = X.copy()
                _X.remove(x)
                Y.extend([[x] + _x for _x in backtrack(_X)])
            return Y
        else:
            return [X]
    return backtrack(nums)
    
    
print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))

#66.06
#30.47