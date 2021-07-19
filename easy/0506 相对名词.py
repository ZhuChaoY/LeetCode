'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别
授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)
输入: [5, 4, 3, 2, 1] 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4",
"5"]解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” 
("Gold Medal", "Silver Medal" and "Bronze Medal"). 余下的两名运动员，我们只需要通
过他们的成绩计算将其相对名次即可。N是一个正整数不会超过10000。所有运动员的成绩都不相同。
'''

def findRelativeRanks(score):
    rank = sorted(score)[::-1]
    rank_dict = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
    hash_map = {}
    for idx, r in enumerate(rank):
        if idx in rank_dict:
            y = rank_dict[idx]
        else:
            y = str(idx + 1)
        hash_map[r] = y
    return [hash_map[x] for x in score]
    
print(findRelativeRanks([5, 4, 3, 2, 1]))
    
#82.26
#47.01
