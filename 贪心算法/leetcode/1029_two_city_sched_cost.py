class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs = sorted(costs, key=lambda x:x[0]-x[1])
        half_n = len(costs) // 2

        res = 0

        for i in range(half_n):
            res += costs[i][0] + costs[i+half_n][1]
        
        return res


        

        
