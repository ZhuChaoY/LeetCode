'''
给定仅有小写字母组成的字符串数组A，返回列表中的每个字符串中都显示的全部字符（包括重复字
符）组成的列表。例如，如果一个字符在每个字符串中出现3次，但不是4次，则需要在最终答案中
包含该字符 3 次。 你可以按任意顺序返回答案.
示例 1： 输入：["bella","label","roller"] 输出：["e","l","l"]
示例 2： 输入：["cool","lock","cook"] 输出：["c","o"]
提示： 1 <= A.length <= 100  1 <= A[i].length <= 100  A[i][j] 是小写字母
'''

def commonChars(words):
    ans = []
    for x in set(words[0]):
        ans += min(word.count(x) for word in words) * x
    return ans
    
print(commonChars(['bella', 'label', 'roller']))
print(commonChars(['cool', 'lock', 'cook']))

#97.40
#5.36