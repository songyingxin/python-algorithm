# -*- coding:utf-8 -*-

class merge_simple:
    """非原地算法实现 """
    def merge(self, arr1, arr2):
        """ 合并两个有序数组 """
        left = 0
        right = 0

        result = []

        while left < len(arr1) and right < len(arr2):
            if arr1[left] <= arr2[right]:
                result.append(arr1[left])
                left += 1
            else:
                result.append(arr2[right])
                right += 1
            
        if left < len(arr1):
            result.extend(arr1[left:])
        
        if right < len(arr2):
            result.extend(arr2[right:])

        return result

    def merge_sort(self, arr):
        """ 算法递归实现 """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.merge(left, right)
    