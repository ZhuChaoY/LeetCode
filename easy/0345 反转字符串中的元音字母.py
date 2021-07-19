'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
输入："hello" 输出："holle"
输入："leetcode" 输出："leotcede"
元音字母不包含字母 "y" 。
'''

def reverseVowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    s = list(s)
    vo_idx = [i for i in range(len(s)) if s[i] in vowels]            
    i, j = 0, len(vo_idx) - 1
    
    while i < j:
        s[vo_idx[i]], s[vo_idx[j]] = s[vo_idx[j]], s[vo_idx[i]]
        i += 1
        j -= 1
    return ''.join(s)

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))
        
#55.71
#10.56 