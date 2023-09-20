class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        help_dict = {}

        res = [-1] * len(nums1)
        stack = []
        for index,val in enumerate(nums2):
            while stack and val > nums2[stack[-1]]:
                pre_index = stack.pop()
                help_dict[nums2[pre_index]] = val
            
            stack.append(index)
        
        for index, val in enumerate(nums1):
            if val in help_dict:
                res[index] = help_dict[val]
        
        return res