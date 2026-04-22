class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 核心思路： 先找到 nums2 的 下一个最大元素，然后再映射到nums1
        help_dict = {}

        res = [-1] * len(nums1)
        stack = []  # 存放 nums2 的元素，从[0:i]单调递减

        for index,val in enumerate(nums2):
            # 将栈中比 val 小的元素都弹出
            while stack and val > nums2[stack[-1]]:
                pre_index = stack.pop()
                help_dict[nums2[pre_index]] = val
            
            stack.append(index)
        
        for index, val in enumerate(nums1):
            if val in help_dict:
                res[index] = help_dict[val]
        
        return res