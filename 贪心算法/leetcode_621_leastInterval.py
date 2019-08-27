class Solution(object):
    def leastInterval(self, tasks, n):

        length = len(tasks)
        if length <= 1:
            return length
        
        # dict: {任务类型：任务次数}
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        
        # 按照出现次数排序
        task_sort = sorted(task_map.items, key=lambda x:x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]

        # 至少需要的最短时间
        result = (max_task_count -1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                result += 1
        
        if result >= length:
            return result
        else:
            return length



