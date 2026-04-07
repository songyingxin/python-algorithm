# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def dfs(node):
            if not node:
<<<<<<< HEAD:二叉树/leetcode/leetcode_easy_145_postorderTraversal.py
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

=======
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
>>>>>>> aee39073896dc72ae9473a4ac3cfc60c2efb46c8:二叉树/leetcode/树的遍历/leetcode_easy_145_postorderTraversal.py
        dfs(root)
        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
            
            res.append(node.val)
        
        return res[::-1]
