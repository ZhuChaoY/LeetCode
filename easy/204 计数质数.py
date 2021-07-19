'''
统计所有小于非负整数 n 的质数的数量。
输入: 10 输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

def countPrimes(n):
     if n < 3:
         return 0   
     else:
         output = [0, 0] + [1] * (n - 2)
         for i in range(2, int(n ** 0.5) + 1): 
             if output[i] == 1:
                 output[i * i : n : i] = [0] * len(output[i * i : n : i])
         return sum(output)
    
print(countPrimes(10))    
print(countPrimes(499979))

#70.80
#5.08

