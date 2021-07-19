'''
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
示例：n = 15,
返回: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
    "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
'''

def fizzBuzz(n):
    ans = [str(i) for i in range(1, n + 1)]
    for i in range(1, n + 1):
        if i % 3 == 0:
            ans[i - 1] = 'Fizz'
            if i % 5 == 0:
                ans[i - 1] += 'Buzz'
        elif i % 5 == 0:
            ans[i - 1] = 'Buzz'
    return ans
     
print(fizzBuzz(15))    
 
#84.85
#57.30 