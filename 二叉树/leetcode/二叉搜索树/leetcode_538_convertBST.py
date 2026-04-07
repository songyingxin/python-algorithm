class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.pre_val = 0
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            
            node.val = self.pre_val + node.val
            self.pre_val = node.val
            dfs(node.left)
            
        
        dfs(root)
        return root


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        pre_val = 0
        stack = []
        node = root

        while node or stack:
            # 先遍历右节点，当右节点存在则入栈
            if node:
                stack.append(node)
                node = node.right
            else:
            # 出栈当前节点，然后处理当前节点后，遍历左节点
                node = stack.pop()
                node.val = node.val + pre_val
                pre_val = node.val

                node = node.left
        
        return root