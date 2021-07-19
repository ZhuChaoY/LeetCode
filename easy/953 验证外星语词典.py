'''
某种外星语也使用英文小写字母，但可能顺序order不同。字母表的顺序是一些小写字母的排列。
给定一组用外星语书写的单词words，以及其字母表的顺序order，只有当给定的单词在这种外星语
中按字典序排列时，返回 true；否则，返回 false。
示例 1：输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true 解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
示例 2：输入：words=["word","world","row"], order="worldabcefghijkmnpqstuvxyz"
输出：false 解释：在该语言的字母表中，'d'位于'l'之后，那么words[0]>words[1]，因此单
词序列不是按字典序排列的。
示例 3：输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false 解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂
规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小。
提示： 1 <= words.length <= 100  1 <= words[i].length <= 20
order.length == 26  在 words[i] 和 order 中的所有字符都是英文小写字母。
'''

def isAlienSorted(words, order):
    order_idx = {c: i for i, c in enumerate(order)}
    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        for k in range(min(len(word1), len(word2))):
            flag = True
            idx1, idx2 = order_idx[word1[k]], order_idx[word2[k]]
            if idx1 < idx2:
                flag = False
                break
            elif idx1 > idx2:
                return False
        if flag and len(word1) > len(word2):
            return False
    return True

        
print(isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'))
print(isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'))
print(isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'))

#96.41
#66.27