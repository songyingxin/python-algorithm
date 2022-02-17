class Solution:
    def combinationSum3(self, k, n):
        def dfs(arr_len, start, sum_val, item):
            if arr_len == k:
                if sum_val == n:
                    result.append(item)
                return
            
            for i in range(start, 10):
                tmp_item = item[:]
                tmp_item.append(i)
                dfs(arr_len+1, i+1, sum_val + i,tmp_item)
        
        result = []
        dfs(0, 1, 0, [])

        return result
            
            

