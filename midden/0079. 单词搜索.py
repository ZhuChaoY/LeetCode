'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，
返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或
垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
 word = "ABCCED"  输出：true
示例 2：输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
 word = "SEE" 输出：true
示例 3： 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
 word = "ABCB"
输出：false
提示： m == board.length n = board[i].length  1 <= m, n <= 6
1 <= word.length <= 15  board 和 word 仅由大小写英文字母组成
进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在board更大的情况下可以更快解决问题？
'''

def exist(board, word):
    m, n = len(board), len(board[0])
    def back(i, j, s):
        if len(s) == 0:
            return True
        v = board[i][j]
        board[i][j] = 0
        if i + 1 < m and board[i + 1][j] == s[0] and back(i + 1, j, s[1: ]):
            return True
        if j + 1 < n and board[i][j + 1] == s[0] and back(i, j + 1, s[1: ]):
            return True
        if i - 1 >= 0 and board[i - 1][j] == s[0] and back(i - 1, j, s[1: ]):
            return True
        if j - 1 >= 0 and board[i][j - 1] == s[0] and back(i, j - 1, s[1: ]):
            return True
        board[i][j] = v
        return False
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if back(i, j, word[1: ]):
                    return True
    return False
    

print(exist([['A']], word = 'A'))
print(exist([['C', 'A', 'A'], ['A', 'A', 'A'], ['B', 'C', 'D']], word = 'AAB'))
print(exist([['A', 'A', 'A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A', 'A', 'A'],
             ['A', 'A', 'A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A', 'A', 'A'],
             ['A', 'A', 'A', 'A', 'A', 'B'], ['A', 'A', 'A', 'A', 'B', 'A']],
             word = 'AAAAAAAAAAAAABB'))
print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            word = 'ABCCED'))
print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            word = 'SEE'))
print(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],
            word = 'ABCB'))

#94.22
#18.36







