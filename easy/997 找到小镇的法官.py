'''
在一个小镇里，按从1到N标记了N个人。传言称，这些人中有一个是小镇上的秘密法官。如果小镇的
法官真的存在，那么：小镇的法官不相信任何人。每个人都信任小镇的法官。只有一个人同时满足
属性1和属性2。给定数组trust，该数组由信任对trust[i]=[a,b]组成，表示标记为a的人信任标
记为b的人。如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
示例 1: 输入：N = 2, trust = [[1,2]] 输出：2
示例 2：输入：N = 3, trust = [[1,3],[2,3]] 输出：3
示例 3：输入：N = 3, trust = [[1,3],[2,3],[3,1]] 输出：-1
示例 4：输入：N = 3, trust = [[1,2],[2,3]] 输出：-1
示例 5： 输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]] 输出：3
提示： 1 <= N <= 1000  trust.length <= 10000  trust[i] 是完全不同的
trust[i][0] != trust[i][1]  1 <= trust[i][0], trust[i][1] <= N
'''

def findJudge(n, trust):
    if n == 1:
        return 1
    map_dict, ban = {}, []
    for a, b in trust:
        if a not in ban:
            ban.append(a)
        if b not in map_dict:
            map_dict[b] = [a]
        else:
            map_dict[b].append(a)
    for k, v in map_dict.items():
        if len(v) == n - 1 and k not in ban:
            return k
    return -1
               
print(findJudge(2, [[1, 2]]))
print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(findJudge(3, [[1, 2], [2, 3]]))
print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

#61.46
#77.92
