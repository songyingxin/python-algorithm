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

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def dfs(nums):
            if not nums:
                return
            
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(nums[:mid])
            node.right = dfs(nums[mid+1:])
            return node

        return dfs(nums)