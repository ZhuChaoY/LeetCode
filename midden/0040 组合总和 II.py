'''
给定candidates和一个目标数 target，找出candidates中所有使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。 
示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:[[1,1,6], [1,2,5], [1,7], [2,6]]
示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 
输出: [[1,2,2], [5]]
提示: 1 <= candidates.length <= 100  1 <= candidates[i] <= 50
1 <= target <= 30
'''

def combinationSum2(candidates, target):
    X = sorted([x for x in candidates if x <= target])
    n = len(X)
    ans = []
    def backtrack(i, S, tmp):
        if S > target:
            return None
        if S == target:
            ans.append(tmp)
            return None
        for j in range(i, n):
            v = X[j]
            if S + v > target:
                break
            if j > i and X[j] == X[j - 1]:
                continue
            backtrack(j + 1, S + v, tmp + [v])
    backtrack(0, 0, [])
    return ans
    
    
print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
print(combinationSum2([1 for i in range(25)], 27))

#70.35
#36.56