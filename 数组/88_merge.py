class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -= 1
            end -= 1

        # 如果 n 没有结束，则需要继续添加，但m 就没有必要，因为其本就在num1中
        while n >= 0:
            nums1[end] = nums2[n]
            end -= 1
            n -= 1
