class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []

        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            
        res[num] = stack[-1] if stack else -1
        stack.append(num)
    
    return [res[num] for num in nums1]