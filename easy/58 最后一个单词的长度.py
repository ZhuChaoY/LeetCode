'''
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
输入: "Hello World" 输出: 5
'''

def lengthOfLastWord(s):
    count = 0
    for x in s[::-1]:
        if x != ' ':
            count += 1
        elif count != 0:
            break
    return count

print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord('Hello World '))        
        
#17.26
#6.93 

