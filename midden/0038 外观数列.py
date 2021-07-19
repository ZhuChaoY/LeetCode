'''
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。 注意：整数序列中的每一项将表示
为一个字符串。「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描
述。前五项如下：
1.     '1'      第一项是数字 1
2.     '11'     描述前一项，这个数是 1 即 “一个 1 ”，记作 11
3.     '21'     描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
4.     '1211'   描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
5.     '111221' 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221
'''

def countAndSay(n):
    if n <= 2:
        return '1' * n
    ans = '11'
    for i in range(n - 2):
        newans = ''
        p = 0
        for q in range(1, len(ans)):
            if ans[q] != ans[p]:
                newans += (str(q - p) + ans[p])
                p = q
        newans += (str(q + 1 - p) + ans[p])
        ans = newans
        
    return ans
    
print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))

#60.59
#9.67