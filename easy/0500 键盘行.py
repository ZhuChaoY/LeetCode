'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
你可以重复使用键盘上同一字符。你可以假设输入的字符串将只包含字母。
'''

def findWords(words):
    s1, s2, s3 = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
    ans = []
    for word in words:
        x = word.lower()
        if x.strip(s1) == '' or x.strip(s2) == '' or x.strip(s3) == '':
            ans.append(word)
    return ans

print(findWords(['Hello', 'Alaska', 'Dad', 'Peace']))
     
#17.38
#5.20