'''
环形公交路线上有n个站，按次序从0到n - 1进行编号。我们已知每一对相邻公交站之间的距离，
distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。
环线上的公交车都可以按顺时针和逆时针的方向行驶。
返回乘客从出发点 start 到目的地 destination 之间的最短距离。
示例 1: 输入：distance = [1,2,3,4], start = 0, destination = 1  输出：1
解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。
示例 2： 输入：distance = [1,2,3,4], start = 0, destination = 2  输出：3 
解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
示例 3： 输入：distance = [1,2,3,4], start = 0, destination = 3  输出：4
解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。
提示： 1 <= n <= 10^4  distance.length == n
0 <= start, destination < n  0 <= distance[i] <= 10^4
'''

def distanceBetweenBusStops(distance, start, destination):
    if start == destination:
        return 0
    else:
        s, d = min(start, destination), max(start, destination)
        l_s, l_n = 0, distance[-1]
        for i in range(len(distance) - 1):
            if i < s or i >= d:
                l_n += distance[i]
            else:
                l_s += distance[i]
        return min(l_s, l_n)
        
print(distanceBetweenBusStops([1, 2, 3, 4], 0, 1))
print(distanceBetweenBusStops([1, 2, 3, 4], 0, 2))
print(distanceBetweenBusStops([1, 2, 3, 4], 0, 3))

#97.02
#80.43