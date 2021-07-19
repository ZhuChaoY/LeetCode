'''
请你帮忙给从1到n的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」索引从1开始
上；你需要返回可能的方案总数。答案可能会很大，请你返回答案模mod 10^9+7之后的结果即可。
示例 1：输入：n = 5 输出：12 解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 
[5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
示例 2：输入：n = 100  输出：682289015
提示： 1 <= n <= 100
'''

def numPrimeArrangements(n):
    if n <= 3:
        return max(n - 1, 1)
    else:
        a, b = 1, 2
        for i in range(4, n + 1):
            flag = True
            j = 2
            while j * j <= i:
                if i % j == 0:
                    flag = False
                    break
                j += 1
            if flag:
                b += 1
            else:
                a += 1
        ans = 1
        for x in range(2, a + 1):
            ans *= x
        for y in range(2, b + 1):
            ans *= y
        return ans % 1000000007
    
print(numPrimeArrangements(5))
print(numPrimeArrangements(100))

#56.57
#5.14