'''
给你一个日志数组 logs。每条日志都是以空格分隔的字串，第一个字为字母与数字混合的标识符。
字母日志：除标识符外，所有字均由小写字母组成 数字日志：除标识符之外，所有字均由数字组成.
请按下述规则将日志重新排序： 所有字母日志都排在数字日志之前。字母日志在内容不同时，忽略
标识符后，按内容字母顺序排序；内容相同时，按标识符排序。数字日志应该保留原来的相对顺序。
返回日志的最终顺序。
示例 1：输入：logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig",
"let3 art zero"] 输出：["let1 art can","let3 art zero","let2 own kit dig",
"dig1 8 1 5 1","dig2 3 6"] 解释： 字母日志的内容都不同，所以顺序为 "art can",
"art zero", "own kit dig"。数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6"。
示例 2：输入：logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog",
"a8 act zoo"] 
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
提示： 1 <= logs.length <= 100  3 <= logs[i].length <= 100  logs[i] 中，字与字
之间都用单个空格分隔题目数据保证logs[i]都有一个标识符，并且在标识符之后至少存在一个字.
'''

def reorderLogFiles(logs):
    is_d = lambda s: 48 <= ord(s) <= 57
    d = [log for log in logs if is_d(log[-1])]
    l = sorted([' '.join(log.split()[1:] + [' '] + log.split()[:1])
                for log in logs if not is_d(log[-1])])
    new_l = [' '.join(log.split()[-1:] + log.split()[:-1]) for log in l]
    return new_l + d
    
print(reorderLogFiles(['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6',
                       'let2 own kit dig', 'let3 art zero']))
print(reorderLogFiles(['a1 9 2 3 1', 'g1 act car', 'zo4 4 7',
                       'ab1 off key dog', 'a8 act zoo']))
print(reorderLogFiles(['dig1 8 1 5 1', 'let1 art zero can', 'dig2 3 6',
                       'let2 own kit dig', 'let3 art zero']))

#90.84
#5.18