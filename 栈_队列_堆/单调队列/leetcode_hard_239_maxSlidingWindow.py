

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        queue = []  # 维护一个单调队列

        # 遍历前k个元素，将当前窗口的最大值下标维护在单调队列中
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        res = [nums[queue[0]]]
        for i in range(k,n):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            while queue[0] <= i-k:
                queue.pop(0)
            
            res.append(nums[queue[0]])
        
        return res