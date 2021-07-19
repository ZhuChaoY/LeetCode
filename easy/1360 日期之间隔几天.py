'''
请你编写一个程序来计算两个日期之间隔了多少天。
日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。
示例 1：输入：date1 = "2019-06-29", date2 = "2019-06-30" 输出：1
示例 2：输入：date1 = "2020-01-15", date2 = "2019-12-31" 输出：15
提示：给定的日期是 1971 年到 2100 年之间的有效日期。
'''

def daysBetweenDates(date1, date2):
    days_1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    days_2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    
    y1, m1, d1 = date1.split('-')
    y2, m2, d2 = date2.split('-')
    y1, m1, d1 = int(y1), int(m1), int(d1)
    y2, m2, d2 = int(y2), int(m2), int(d2)
    
    _y = min(y1, y2)
    diff1 = 0
    for y in range(_y, y1):
        if y % 4 != 0:
            diff1 += 365
        else:
            diff1 += 366
    if y1 % 4 != 0:
        diff1 += days_1[m1 - 1] + d1
    else:
        diff1 += days_2[m1 - 1] + d1
    if y1 == 2100 and m1 >= 3:
        diff1 -= 1
    diff2 = 0
    for y in range(_y, y2):
        if y % 4 != 0:
            diff2 += 365
        else:
            diff2 += 366
    if y2 % 4 != 0:
        diff2 += days_1[m2 - 1] + d2
    else:
        diff2 += days_2[m2 - 1] + d2
    if y2 == 2100 and m2 >= 3:
        diff2 -= 1
    return abs(diff1 - diff2)
    
print(daysBetweenDates('2019-06-29', '2019-06-30'))
print(daysBetweenDates('2020-01-15', '2019-12-31'))

#96.87
#69.53


