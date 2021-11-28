'''
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），
整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、
"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，
这些地址可以通过在 s 中插入 '.' 来形成。你不能重新排序或删除 s 中的任何数字。
你可以按 任何 顺序返回答案。
示例 1：输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：输入：s = "0000"
输出：["0.0.0.0"]
示例 3：输入：s = "1111"
输出：["1.1.1.1"]
示例 4：输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
提示： 0 <= s.length <= 20  s 仅由数字组成
'''

def restoreIpAddresses(s):
    n = len(s)
    if n < 4 or n > 12:
        return []
    elif n == 4:
        return ['.'.join(list(s))]
    elif n == 12:
        ans = []
        for i in range(4):
            tmp = s[3 * i: 3 * i + 3]
            if 100 <= int(tmp) <= 255:
                ans.append(tmp)
            else:
                return []
        return ['.'.join(ans)]
    else:
        ans = [[s[0]]]
        for x in s[1: ]:
            new_ans = []
            for an in ans:
                if len(an) < 4:
                    new_ans.append(an + [x])
                end = an[-1]
                if end != '0' and int(end + x) <= 255:
                    an[-1] += x
                    new_ans.append(an)
            ans = new_ans
    return ['.'.join(x) for x in ans if len(x) == 4]
    
    
print(restoreIpAddresses('25525511135'))
print(restoreIpAddresses('0000'))
print(restoreIpAddresses('1111'))
print(restoreIpAddresses('010010'))
print(restoreIpAddresses('101023'))

#83.90
#25.85

