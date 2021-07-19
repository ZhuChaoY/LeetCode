'''
一副牌，每张牌上都写着一个整数。你需要选定一个数字X，使我们可以将整副牌按下述规则分成1组
或更多组：每组都有X张牌。组内所有的牌上都写着相同的整数。仅当你可选的X>=2时返回true。
示例 1：输入：[1,2,3,4,4,3,2,1] 输出：true 解释：[1,1]，[2,2]，[3,3]，[4,4]
示例 2：输入：[1,1,1,2,2,2,3,3] 输出：false 解释：没有满足要求的分组。
示例 3：输入：[1] 输出：false 解释：没有满足要求的分组。
示例 4：输入：[1,1] 输出：true 解释：可行的分组是 [1,1]
示例 5：输入：[1,1,2,2,2,2] 输出：true 解释：可行的分组是 [1,1]，[2,2]，[2,2]
提示： 1 <= deck.length <= 10000  0 <= deck[i] < 10000
'''

def hasGroupsSizeX(deck):
    count = {}
    for x in deck:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    lens = count.values()
    m = min(lens)
    if m == 1:
        return False
    else:
        if m <= 3:
            y = [m]
        else:
            y = [i for i in range(2, m - 1) if m % i == 0]
            if len(y) == 0:
                y = [m]
        for i in y:
            flag = True
            for l in lens:
                if l % i != 0:
                    flag = False
                    break
            if flag:
                return True
        return False
    
print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(hasGroupsSizeX([1]))
print(hasGroupsSizeX([1,1]))
print(hasGroupsSizeX([1,1,2,2,2,2]))
print(hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))

#71.40
#34.46
