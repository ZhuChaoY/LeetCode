'''
给你一个字符串s，请你根据下面的算法重新构造字符串：
从s中选出最小的字符，将它接在结果字符串的后面。
从s剩余字符中选出最小的字符，且该字符比上一个添加的字符大，将它接在结果字符串后面。
重复步骤2，直到你没法从s中选择字符。从s中选出最大的字符，将它接在结果字符串的后面。
从s剩余字符中选出最大的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤5，直到你没法从s中选择字符。重复步骤1到6，直到s中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，选择其中任意一个，并将其添加到结果字符串。
请你返回将 s 中字符重新排序后的 结果字符串 。
示例 1：输入：s = "aaaabbbbcccc" 输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
示例 2： 输入：s = "rat" 输出："art" 
解释：单词 "rat" 在上述算法重排序以后变成 "art"
示例 3：输入：s = "leetcode" 输出："cdelotee"
示例 4：输入：s = "ggggggg" 输出："ggggggg"
示例 5： 输入：s = "spo"  输出："ops"
提示： 1 <= s.length <= 500  s 只包含小写英文字母。
'''

def sortString(s):
    s_dict = {}
    for x in s:
        if x not in s_dict:
            s_dict[x] = 1
        else:
            s_dict[x] += 1
    n = len(s)
    ans = ''
    while True:
        keys = sorted(s_dict.keys())
        ans += ''.join(keys)
        if len(ans) == n:
            break
        for key in keys:
            if s_dict[key] == 1:
                del s_dict[key]
            else:
                s_dict[key] -= 1
        keys = sorted(s_dict.keys())
        ans += ''.join(keys[::-1])
        if len(ans) == n:
            break
        for key in keys:
            if s_dict[key] == 1:
                del s_dict[key]
            else:
                s_dict[key] -= 1
    return ans
        
    
print(sortString('aaaabbbbcccc'))
print(sortString('rat'))
print(sortString('leetcode'))
print(sortString('ggggggg'))
print(sortString('spo'))
print(sortString('gtqxozxzrssrzxzoxqtg'))

#97.80
#26.10

