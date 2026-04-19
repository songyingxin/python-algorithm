class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        help_dict = {}
        for num_1 in nums1:
            for num_2 in nums2:
                now_val = num_1 + num_2
                if now_val in help_dict:
                    help_dict[now_val] += 1
                else:
                    help_dict[now_val] = 1
        
        res = 0
        for num_3 in nums3:
            for num_4 in nums4:
                sub_val = 0-num_3-num_4
                if sub_val in help_dict:
                    res += help_dict[sub_val]
        
        return res