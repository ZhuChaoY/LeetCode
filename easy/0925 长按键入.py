'''
你的朋友正在使用键盘输入他的名字name。偶尔，在键入字符c时，按键可能会被长按，而字符可能
被输入 1 次或多次。你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其
中一些字符可能被长按），那么就返回 True。
示例 1：输入：name="alex", typed="aaleex" 输出：true 'alex'中的 'a' 和 'e'被长按。
示例 2：输入：name="saeed", typed="ssaaedd" 输出：false 
'e'一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：输入：name = "leelee", typed = "lleeelee" 输出：true
示例 4：输入：name="laiden", typed="laiden" 输出：true长按名字中的字符并不是必要的。
提示： name.length <= 1000 typed.length<=1000  name和typed的字符都是小写字母。
'''

def isLongPressedName(name, typed):
    n, m = len(name), len(typed)
    if name == typed:
        return True
    elif n > m or n * m == 0:
        return False
    else:
        p, q = 0, 0
        while p < n and q < m:
            v = name[p]
            if typed[q] != v:
                return False
            else:
                dn, dt = 1, 1
                for i in range(1, n - p):
                    if name[p + i] == v:
                        dn += 1
                    else:
                        break
                for j in range(1, m - q):
                    if typed[q + j] == v:
                        dt += 1
                    else:
                        break
                if dt < dn:
                    return False
                p += dn
                q += dt
        return p == n and q == m
    
print(isLongPressedName('alex', 'aaleex'))
print(isLongPressedName('saeed', 'ssaaedd'))
print(isLongPressedName('leelee', 'lleeelee'))
print(isLongPressedName('laiden', 'laiden'))
print(isLongPressedName('alex', 'aaleexa'))
print(isLongPressedName('pyplrz', 'ppyypllr'))
print(isLongPressedName('saeedi', 'ssaaeediixxxiii'))

#49.88
#8.76


