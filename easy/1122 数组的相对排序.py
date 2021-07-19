'''
给你两个数组，arr1 和 arr2， arr2 中的元素各不相同 arr2 中的每个元素都出现在 arr1 中
对arr1中的元素进行排序，使arr1中项的相对顺序和arr2中的相对顺序相同。未在 arr2 中出现
过的元素需要按照升序放在 arr1 的末尾
示例： 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
提示： 1 <= arr1.length, arr2.length <= 1000   0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同  arr2 中的每个元素 arr2[i] 都出现在 arr1 中
'''

def relativeSortArray(arr1, arr2):
    n = len(arr2)
    sort_dict = dict(zip(arr2, range(n)))
    count_dict = {n: []}
    for x in arr1:
        if x in sort_dict:
            y = sort_dict[x]
            if y not in count_dict:
                count_dict[y] = [x, 1]
            else:
                count_dict[y][1] += 1
        else:
            count_dict[n] += [x]
    ans = []
    for y in range(n):
        tmp = count_dict[y]
        ans += [tmp[0]] * tmp[1]
    ans += sorted(count_dict[n])
    return ans
    
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))

#99.59
#13.23