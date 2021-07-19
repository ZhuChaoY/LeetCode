'''
给定一个Excel表格中的列名称，返回其相应的列序号。 例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

输入: "A" 输出: 1
输入: "AB" 输出: 28
输入: "ZY" 输出: 701
'''

def titleToNumber(s):
     str_dict = dict(zip([chr(i) for i in range(65, 91)], range(1, 27)))
     n, ans = len(s), 0
     for i in range(n):
         ans += str_dict[s[n - 1 - i]] * 26 ** i
     return ans
 
print(titleToNumber('A'))
print(titleToNumber('AB'))
print(titleToNumber('ZY'))    
    
#84.15
#91.15
