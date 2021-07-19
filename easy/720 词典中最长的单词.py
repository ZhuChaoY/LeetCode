'''
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典
中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。 
若无答案，则返回空字符串.
输入： words = ["w","wo","wor","worl", "world"] 输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
输入： words = ["a", "banana", "app", "appl", "ap", "apply", "apple"] 
输出："apple" 解释： "apply"和"apple"由词典中的单词组成。但"apple"字典序小于"apply"。
输入的字符串只包含小写字母。 words数组长度范围[1,1000]。 words[i]的长度范围为[1,30]。
'''

def longestWord(words):
    words.sort()
    temp = ['']
    for word in words:
        if word[:-1] in temp:
            temp.append(word)
    max_l = max([len(x) for x in temp])
    return min([x for x in temp if len(x) == max_l])

print(longestWord(['w', 'wo', 'wor', 'worl', 'world']))
print(longestWord(['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple']))
    
#53.38
#54.33
