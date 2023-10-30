class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        
        index = 0
        while index < n:
            sum_gas = 0
            sum_cost = 0

            count = 0
            while count < n:
                j = (index+count) % n
                sum_cost += cost[j]
                sum_gas += gas[j]

                if sum_gas < sum_cost:
                    break
                
                count += 1
            
            if count == n:
                return index
            else:
                index = index + count + 1
        
        return -1