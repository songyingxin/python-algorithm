class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(item, start_index):
            if len(item) == k:
                res.append(tuple(item))
                return
            
            # 减枝操作，去掉也能通过
            if len(item) + (n-start_index+1) < k:
                return 

            for i in range(start_index, n+1):
                dfs(item+[i], i+1)

        dfs([], 1)
        return res