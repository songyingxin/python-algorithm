class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtracking(item, k, start):
            if len(item) == k:
                result.append(tuple(item))
                return
            
            # 减枝操作
            if len(item) + (n-start+1) < k:
                return 

            for index in range(start, n+1):

                tmp_item = item[:]
                tmp_item.append(index)
                backtracking(tmp_item, k, index+1)

        result = []
        backtracking([], k, 1)
        return result
