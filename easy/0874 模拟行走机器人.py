'''
机器人在XY网格平面上行走，从点(0, 0)处开始出发，面向北方。该机器人可以接收以下三种类型
commands ：-2 ：向左转90度  -1 ：向右转90度  1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物obstacles。第i个障碍物位于网格点obstacles[i]=(xi, yi)。
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路
线的其余部分。返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。
（即，如果距离为 5 ，则返回 25 ） 注意：北表示 +Y 方向。 东表示 +X 方向。
南表示 -Y 方向。 西表示 -X 方向。
示例 1： 输入：commands = [4,-1,3], obstacles = [] 输出：25
解释： 机器人开始位于 (0, 0)： 1. 向北移动 4 个单位，到达 (0, 4) 2. 右转
3. 向东移动 3 个单位，到达 (3, 4) 距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25
示例 2： 输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]] 输出：65
解释：机器人开始位于 (0, 0)：  1. 向北移动 4 个单位，到达 (0, 4) 2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4) 4. 左转
5. 向北走 4 个单位，到达 (1, 8) 距离原点最远的是 (1, 8) ，距离为 1 + 64 = 65
提示: 1 <= commands.length <= 104
commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
0 <= obstacles.length <= 104 -3 * 104 <= xi, yi <= 3 * 104 答案保证小于 231
'''

def robotSim(commands, obstacles):
    obstacleSet = set(map(tuple, obstacles))
    D = ((1, 1), (0, 1), (1, -1), (0, -1))
    xy, ans, k = [0, 0], 0, 0
    for cm in commands:
        if cm == -2:
            k = (k - 1) % 4
        elif cm == -1:
            k = (k + 1) % 4
        else:
            d, f = D[k]       
            for i in range(cm):
                xy[d] += f
                if tuple(xy) in obstacleSet:
                    xy[d] -= f
                    break
            ans = max(xy[0] ** 2 + xy[1] ** 2, ans)
    return ans
    
print(robotSim([4,-1,3], []))
print(robotSim([4,-1,4,-2,4], [[2, 4]]))

#55.76
#16.89



