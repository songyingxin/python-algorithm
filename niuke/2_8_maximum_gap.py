# -*- coding:utf-8 -*-

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        arr_max = max(nums)
        arr_min = min(nums)
        arr_len = len(nums)

        if arr_max == arr_min:
            return 0

        bucket_num = arr_len + 1   # N + 1 个桶

        has_num = [False for i in range(bucket_num)]  # 第i个桶中是否有数字
        sub_max = [float('-inf') for i in range(bucket_num)]   # 第i个桶中的最大值
        sub_min = [float('inf') for i in range(bucket_num)]  # 第i个桶中的最小值

        """遍历数组，将数据装桶 """
        for i in range(arr_len):
            bid = self.which_bucket(nums[i], arr_len, arr_min, arr_max)
            has_num[bid] = True
            sub_max[bid] = max(sub_max[bid], nums[i])
            sub_min[bid] = min(sub_min[bid], nums[i])

        """ 下一个桶有数中的最小值与上一个桶的最大值比较 """
        result = 0
        last_max = sub_max[0]
        for i in range(1, bucket_num):
            if has_num[i]:
                result = max(result, sub_min[i] - last_max)
                last_max = sub_max[i]
        
        return result
    
    def which_bucket(self, num, arr_len, arr_min, arr_max):
        """ 判断 num 属于第几个桶 """
        return int((num - arr_min) * arr_len / (arr_max - arr_min))


if __name__ == "__main__":
    arr = [6,0,9,12]
    # arr = [3, 6, 9, 1]

    print(Solution().maximumGap(arr))
