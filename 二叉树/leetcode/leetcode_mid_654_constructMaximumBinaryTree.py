


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(nums):
            if not nums:
                return
            max_val = max(nums)
            max_val_index = nums.index(max_val)

            node = TreeNode(max_val)
            node.left = dfs(nums[:max_val_index])
            node.right = dfs(nums[max_val_index+1:])

            return node
        
        return dfs(nums)