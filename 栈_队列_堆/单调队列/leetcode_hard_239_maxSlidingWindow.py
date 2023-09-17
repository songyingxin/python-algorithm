import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        queue = collections.deque()

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
                queue.popleft()
            
            res.append(nums[queue[0]])
        
        return res