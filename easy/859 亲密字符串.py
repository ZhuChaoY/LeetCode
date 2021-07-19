'''
给定两个由小写字母构成的字符串A和B，只要我们可以通过交换A中的两个字母得到与B相等的结果，
就返回 true ；否则返回 false 。交换字母的定义是取两个下标i和j（下标从0开始），
只要i!=j就交换A[i]和A[j]处的字符。在 "abcd"中交换下标0和下标2的元素可以生成"cbad"。
示例 1： 输入： A = "ab", B = "ba" 输出： true
解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。
示例 2： 输入： A = "ab", B = "ab" 输出： false
解释： 你只能交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 不相等。
示例 3: 输入： A = "aa", B = "aa" 输出： true 
解释： 你可以交换 A[0] = 'a'和A[1] = 'a' 生成 "aa"，此时 A 和 B 相等。
示例 4：输入： A = "aaaaaaabc", B = "aaaaaaacb" 输出： true
示例 5： 输入： A = "", B = "aa" 输出： false
提示： 0 <= A.length <= 20000 0 <= B.length <= 20000 A 和 B 仅由小写字母构成。
'''

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    _s, _g = [], []
    for i in range(len(s)):
        if s[i] != goal[i]:
            if len(_s) == 2:
                return False
            _s.append(s[i])
            _g.append(goal[i])
    if len(_s) == 0:
        return len(s) != len(set(s))
    elif len(_s) == 1:
        return False
    else:
        return _s == _g[::-1]
    
    
print(buddyStrings('ab', 'ba'))    
print(buddyStrings('ab', 'ab'))  
print(buddyStrings('aa', 'aa'))  
print(buddyStrings('aaaaaaabc', 'aaaaaaacb'))  
print(buddyStrings('', 'aa'))  

#92.61
#47.03