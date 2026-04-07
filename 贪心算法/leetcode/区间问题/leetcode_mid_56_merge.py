class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 按照第一个数字进行排序
        sort_nums = sorted(intervals, key=lambda x:x[0])

        # 不断扩充第二个数值
        res = [sort_nums[0]]
        for num in sort_nums[1:]:
            if num[0] <= res[-1][1]:
                tmp = res.pop()
                res.append([tmp[0], max(num[1], tmp[1])])
            else:
                res.append(num)
        return res