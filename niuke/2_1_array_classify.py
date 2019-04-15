# -*- coding:utf-8 -*-

def classify_arr(arr, num):

    left = 0   # 0- left 存储小于num的元素 
    
    for i in range(len(arr)):
        if arr[i] < num:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1


if __name__ == "__main__":
    arr = [45,2,5,78,2,87,5,4,7,23,45,56,89]
    classify_arr(arr, 10)
    print(arr)