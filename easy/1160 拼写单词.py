'''
给你一份词汇表（字符串数组）words和一张『字母表』（字符串）chars。假如你可以用chars中
的字母（字符）拼写出 words中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。
示例 1：输入：words = ["cat","bt","hat","tree"], chars = "atach"  输出：6
解释：  可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：words = ["hello","world","leetcode"], chars="welldonehoneyr" 输出：10
解释： 可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
提示：1 <= words.length <= 1000   1 <= words[i].length, chars.length <= 100
'''

def countCharacters(words, chars):
    c_dict = {}
    for c in chars:
        if c not in c_dict:
            c_dict[c] = 1
        else:
            c_dict[c] += 1
    ans = 0
    for word in words:
        _c_dict = c_dict.copy()
        flag = True 
        for w in word:
            if w not in _c_dict or _c_dict[w] == 0:
                flag = False
                break
            else:
                _c_dict[w] -= 1
        if flag:
            ans += len(word)
    return ans
                    
print(countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach'))
print(countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr'))

#100
#6.83