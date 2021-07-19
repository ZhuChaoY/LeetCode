'''
给定一个单词，你需要判断单词的大写使用是否正确。 我们定义，在以下情况时，单词的大写用法
是正确的：全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。	
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。 
否则，我们定义这个单词没有正确使用大写字母。
输入: "USA" 输出: True
输入: "FlaG" 输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
'''

def detectCapitalUse(word):
    hash_map = {}
    for i in range(ord('a'), ord('z') + 1):
        hash_map[chr(i)] = 0
    for i in range(ord('A'), ord('Z') + 1):
        hash_map[chr(i)] = 1
    if len(word) == 1:
        return True
    start = word[0]
    if hash_map[start] == 1:
        if len(set([hash_map[x] for x in word[1:]])) == 1:
            return True
        else:
            return False
    else:
        for x in word[1:]:
            if hash_map[x] == 1:
                return False
        return True

print(detectCapitalUse('USA'))
print(detectCapitalUse('FlaG'))
print(detectCapitalUse('flag'))    

#48.77
#5.35