# -*- coding:utf-8 -*-

import util
class BigHeapSort:

    def heap_sort(self, arr):
        if len(arr) < 2:
            return;
        for i in range(len(arr)):
            self.heap_insert(arr, i)
        size = len(arr)
        arr[0], arr[size-1] = arr[size-1], arr[0]
        size -= 1
        while size > 0:
            self.heapify(arr, 0, size)
            arr[0], arr[size-1] = arr[size-1], arr[0]
            size -= 1
        
    
    def heap_insert(self, arr, index):
        """ 大根堆的构造, 在[0, index] 处构造大根堆 """
        father = int((index-1)/2)
        while arr[index] > arr[father] :
            arr[father], arr[index]  = arr[index], arr[father]
            index = father
            father = int((index-1)/2)
    
    def heapify(self, arr, index, size):
        """ 大根堆的调整 ， 对[0, size-1]区间进行调整"""
        left = index * 2 + 1  # 根节点的左孩子
        while left < size:
            # 左右孩子中较大的那个
            larger = left + 1 if left + 1 < size and arr[left+1] > arr[left] else left  
            # 若当前元素与左右孩子中较大的那个相等，则不需要下沉
            larger = larger if arr[larger] > arr[index] else index   
            if larger == index:
                break
            
            arr[larger], arr[index] = arr[index], arr[larger]
            index = larger
            left = index * 2 + 1


if __name__ == "__main__":
    test_time = 5000
    max_size = 10
    max_value = 100
    min_value = 0
    for i in range(test_time):
        arr = util.get_random_array(max_size, min_value, max_value)
        arr1 = arr.copy()
        predict = BigHeapSort().heap_sort(arr)

        if arr != sorted(arr1):
            print("the false sample is {}".format(arr1))
            print("the false predict is {}".format(arr))
            break
