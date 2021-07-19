'''
给定段落(paragraph)和禁用单词列表(banned)。返回出现次数最多，同时不在禁用列表中的单词。
题目保证至少有一个词不在禁用列表中，而且答案唯一。
禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
输入: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"] 输出: "ball" 解释:  "hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，它是段落里出现次数最多的，不在禁用列表中。 
所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略比如 "ball,"， 
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
提示： 1 <= 段落长度 <= 1000 0 <= 禁用单词个数 <= 100 1 <= 禁用单词长度 <= 10
答案唯一, 都是小写字母(即使在paragraph里是大写的，即使是一些特定的名词，答案都是小写的。
paragraph 只包含字母、空格和下列标点符号!?',;. 不存在没有连字符或者带有连字符的单词。
单词里只包含字母，不会出现省略号或者其他标点符号。
'''

def mostCommonWord(paragraph, banned):
    p = paragraph.lower()
    for s in ['!', '?', '\'', ',', ';', '.']:
        p = p.replace(s, ' ')
    words = p.split()
    count = {}
    for word in words:
        if word not in banned:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    ans, m = '', 0
    for key, value in count.items():
        if value > m:
            m = value
            ans = key
    return ans
    
print(mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.',
                     ['hit']))

#64.44
#55.02