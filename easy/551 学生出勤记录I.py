'''
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：'A' : Absent，
缺勤 'L' : Late，迟到 'P' : Present，到场. 如果一个学生的出勤记录中不超过一个'A'(缺
勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。你需要根据这个学生的出勤记录判
断他是否会被奖赏。
输入: "PPALLP" 输出: True
输入: "PPALLL" 输出: False
'''

def checkRecord(s):
    n_A, n_L = 0, 0
    for x in s:
        if x == 'A':
            n_A += 1
            n_L = 0
        elif x == 'L':
            n_L += 1
        else:
            n_L = 0
        if n_A == 2 or n_L == 3:
            return False
    return True

print(checkRecord('PPALLP'))
print(checkRecord('PPALLL'))
            
#96.83
#5.61  