'''
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的
名字用字符串表示。你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个
，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
输入: ["Shogun", "Tapioca Express", "Burger King", "KFC"] ["Piatti", "The 
      Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"] 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
输入: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
     ["KFC", "Shogun", "Burger King"] 输出: ["Shogun"] 解释: 他们共同喜爱且具有最
     小索引和的餐厅是“Shogun”, 它有最小的索引和1(0+1)。
两个列表的长度范围都在 [1, 1000]内。 两个列表中的字符串的长度将在[1，30]的范围内。
下标从0开始，到列表的长度减1。 两个列表都没有重复的元素。
'''

def findRestaurant(list1, list2):
    S = list(set(list1) & set(list2))
    if len(S) <= 1:
        return S
    dict1 = dict(zip(list1, range(len(list1))))
    dict2 = dict(zip(list2, range(len(list2))))
    ans, temp = [], 10000
    for s in S:
        n = dict1[s] + dict2[s]
        if n < temp:
            ans = [s]
            temp = n
        elif n == temp:
            ans.append(s)
    return ans

print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["Piatti", "The Grill at Torrey Pines",
                      "Hungry Hunter Steakhouse", "Shogun"]))
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["KFC", "Shogun", "Burger King"]))

#98.67
#5.05
