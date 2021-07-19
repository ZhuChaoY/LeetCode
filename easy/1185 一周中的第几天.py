'''
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。输入为三个整数：day、month
和 year，分别表示日、月、年。您返回的结果必须是这几个值中的一个 {"Sunday", "Monday",
"Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
示例 1：输入：day = 31, month = 8, year = 2019  输出："Saturday"
示例 2：输入：day = 18, month = 7, year = 1999 输出："Sunday"
示例 3：输入：day = 15, month = 8, year = 1993 输出："Sunday"
提示： 给出的日期一定是在 1971 到 2100 年之间的有效日期。 (1971.1.1是周五)
'''

def dayOfTheWeek(day, month, year):
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    days_1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    days_2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    diff = 0
    for y in range(1971, year):
        if y % 4 != 0:
            diff += 365
        else:
            diff += 366
    if year % 4 != 0:
        diff += days_1[month - 1] + day
    else:
        diff += days_2[month - 1] + day
    if year == 2100 and month >= 3:
        diff -= 1
    return week[(diff + 4) % 7]

print(dayOfTheWeek(1, 1, 1971))
print(dayOfTheWeek(31, 8, 2019))
print(dayOfTheWeek(18, 7, 1999))
print(dayOfTheWeek(15, 8, 1993))

#99.51
#38.72