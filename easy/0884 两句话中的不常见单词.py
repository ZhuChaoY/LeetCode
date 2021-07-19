'''
给定两个句子A和B.（句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中没有出现，那这个单词就是不常见的。
返回所有不常用单词的列表。您可以按任何顺序返回列表。
示例 1： 输入：A = "this apple is sweet", B = "this apple is sour" 
输出：["sweet","sour"]
示例 2： 输入：A = "apple apple", B = "banana" 输出：["banana"]
提示： 0 <= A.length <= 200 0 <= B.length <= 200 A 和 B 都只包含空格和小写字母。
'''

def uncommonFromSentences(s1, s2):
    ban, l1, l2 = [], [], []
    for x in s1.split():
        if x not in ban:
            if x not in l1:
                l1.append(x)
            else:
                l1.remove(x)
                ban.append(x)
    for x in s2.split():
        if x not in ban:
            if x not in l2:
                l2.append(x)
            else:
                l2.remove(x)
                ban.append(x)
    return list(((set(l1) - set(l2)) | (set(l2) - set(l1))) - set(ban))
    
print(uncommonFromSentences('this apple is sweet', 'this apple is sour'))
print(uncommonFromSentences('apple apple', 'banana'))
print(uncommonFromSentences('fo ly ly', 'fo fo etc'))

#89.73
#5.13