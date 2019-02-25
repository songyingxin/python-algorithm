# -*- coding:utf-8 -*-


def max_gap(arr):
    """ 获取无序数组排序后相邻元素间的最大差值 
    Retuns:
        0: 数组长度小于2 或 数组最大值等于最小值
        max_value:  最大差值
    """
    if len(arr) < 2:
        return 0

    arr_max = max(arr)
    arr_min = min(arr)
    arr_len = len(arr)

    if arr_min == arr_max:
        return 0

    has_num = [False for i in range(arr_len+1)]
    sub_max = [float('-inf') for i in range(arr_len+1)]
    sub_min = [float('inf') for i in range(arr_len+1)]

    """ 装桶 """
    for i in range(arr_len):
        bid = bucket(arr[i], arr_len, arr_min, arr_max)
        sub_max[bid] = max(sub_max[bid], arr[i])
        sub_min[bid] = min(sub_min[bid], arr[i])
        has_num[bid] = True
    
    """ 下一个桶的最小值与上一个桶的最大值比较 """
    res = 0
    last_max = sub_max[0]
    for i in range(1, arr_len):
        if has_num[i]:
            res = max(res, sub_min[i] - last_max)
            last_max = sub_max[i]
    
    return res



def bucket(num, arr_len, arr_min, arr_max):
    return int((num - arr_min) * arr_len / (arr_max - arr_min))


if __name__ == "__main__":
    arr = [6,0,9,12]

    print(max_gap(arr))