'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次.
示例 1: 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2: 输入: strs = [""]  输出: [[""]]
示例 3: 输入: strs = ["a"]  输出: [["a"]]
提示：1 <= strs.length <= 10^4  0 <= strs[i].length <= 100 strs[i] 仅包含小写字母
'''

def groupAnagrams(strs):
    s_dict = {}
    for s in strs:
        _s = ''.join(sorted(s))
        if _s not in s_dict:
            s_dict[_s] = [s]
        else:
            s_dict[_s].append(s)
    return list(s_dict.values())
    
    
print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(groupAnagrams(['']))
print(groupAnagrams(['a']))

#100
#65.55