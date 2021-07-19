'''
给你一个由一些多米诺骨牌组成的列表 dominoes。如果其中某一张多米诺骨牌可以通过旋转0度
或180度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。形式上，dominoes[i] = [a, b]
和dominoes[j]=[c, d]等价的前提是a==c且b==d，或是a==d且b==c。在0 <=i<j<dominoes.
length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
示例：输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]  输出：1
提示： 1 <= dominoes.length <= 40000   1 <= dominoes[i][j] <= 9
'''

def numEquivDominoPairs(dominoes):
    count_dict = {}
    for X in dominoes:
        x1 = str(X[0]) + ' ' + str(X[1])
        if x1 not in count_dict:
            count_dict[x1] = 1
        else:
            count_dict[x1] += 1
        if X[0] != X[1]:
            x2 = str(X[1]) + ' ' + str(X[0])
        else:
            x2 = str(X[0]) + '-' + str(X[1])
        if x2 not in count_dict:
            count_dict[x2] = 1
        else:
            count_dict[x2] += 1
    ans = 0
    for y in count_dict.values():
        ans += y * (y - 1) // 2
    return ans // 2
    
print(numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6], [1, 2]]))
print(numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
print(numEquivDominoPairs([[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]))

#95.63
#98.54