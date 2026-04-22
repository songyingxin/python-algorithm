class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        cur_sum = 0 # 当前累计的剩余油量
        start = 0 # 起始位置

        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]

            if cur_sum < 0:
                start = i+1
                cur_sum = 0

        return start