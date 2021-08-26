'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
有效括号组合需满足：左括号必须以正确的顺序闭合。
示例 1：输入：n = 3  输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：输入：n = 1  输出：["()"]
提示： 1 <= n <= 8
'''

def generateParenthesis(n):
    ans = ['(']
    while len(ans[0]) < 2 * n:
        tmp = []
        for x in ans:
            l = x.count('(')
            r = len(x) - l
            if l == n:
                tmp.append(x + ')')
            elif r == l:
                tmp.append(x + '(')
            else:
                tmp.extend([x + '(', x + ')'])
        ans = sorted(set(tmp))
    return ans
    

print(generateParenthesis(1))
print(generateParenthesis(2))    
print(generateParenthesis(3))
print(generateParenthesis(4))

#66.81
#98.01