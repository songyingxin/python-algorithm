class Solution:
    def sortedArrayToBST(self, nums):

        def dfs(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            head = TreeNode(nums[mid])
            head.left = dfs(nums, start, mid-1)
            head.right = dfs(nums, mid+1, end)

            return head

        return dfs(nums, 0, len(nums) - 1)
