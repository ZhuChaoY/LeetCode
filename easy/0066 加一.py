'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
输入: [1,2,3] 输出: [1,2,4] 解释: 输入数组表示数字 123。
输入: [4,3,2,1] 输出: [4,3,2,2] 解释: 输入数组表示数字 4321。
'''

def plusOne(digits):
    n = len(digits)
    i = 1
    while i <= n:
        if digits[-i] != 9:
            digits[-i] += 1
            return digits
        else:
            digits[-i] = 0
            i += 1
    return [1] + digits
    
print(plusOne([1, 2, 3]))  
print(plusOne([4, 3, 2, 1]))     

#99.46
#64.94