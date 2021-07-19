'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地
块上，它们会争夺水源，两者都会死去。给定一个花坛（表示为一个数组包含0和1，其中0表示没种
植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？
能则返回True，不能则返回False。
输入: flowerbed = [1,0,0,0,1], n = 1 输出: True
输入: flowerbed = [1,0,0,0,1], n = 2 输出: False
数组内已种好的花不会违反种植规则。 输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
'''

def canPlaceFlowers(flowerbed, n):
    s, k = 0, 1
    for x in flowerbed + [0, 1]:
        if x == 0:
            k += 1
        else:
            s += (k - 1) // 2
            k = 0
    return n <= s
            
print(canPlaceFlowers([1, 0, 0, 0, 1], 1))            
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))    

#55.95
#5.19