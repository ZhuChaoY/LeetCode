'''
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，
找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates中的数字无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
示例 1： 输入: candidates = [2,3,6,7], target = 7  输出: [[7],[2,2,3]]
示例 2： 输入: candidates = [2,3,5], target = 8 输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3： 输入: candidates = [2], target = 1 输出: []
示例 4： 输入: candidates = [1], target = 1 输出: [[1]]
示例 5： 输入: candidates = [1], target = 2 输出: [[1,1]]
提示： 1 <= candidates.length <= 30  1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。  1 <= target <= 500
'''

def combinationSum(candidates, target):
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
            backtrack(j, S + v, tmp + [v])
    backtrack(0, 0, [])
    return ans


print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
print(combinationSum([1], 1))
print(combinationSum([1], 2))

#81.31
#36.32