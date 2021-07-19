'''
给你一个按YYYY-MM-DD格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。
每个月的天数与现行公元纪年法（格里高利历）一致。
示例 1：输入：date = "2019-01-09" 输出：9
示例 2：输入：date = "2019-02-10" 输出：41
示例 3：输入：date = "2003-03-01" 输出：60
示例 4：输入：date = "2004-03-01" 输出：61
提示： date.length == 10 date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。
'''

def dayOfYear(date):
    days_1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    days_2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    y, m, d = date.split('-')
    y, m, d = int(y), int(m), int(d)
    if y % 4 != 0:
        return days_1[m - 1] + d
    else:
        return days_2[m - 1] + d
    
print(dayOfYear('2019-01-09'))
print(dayOfYear('2019-02-10'))
print(dayOfYear('2003-03-01'))
print(dayOfYear('2004-03-01')) 

#73.91
#35.15