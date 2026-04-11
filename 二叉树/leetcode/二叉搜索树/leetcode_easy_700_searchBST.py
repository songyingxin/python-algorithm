

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.target = val
        def dfs(node):
            if not node:
                return 
            
            if node.val == self.target:
                return node
            elif node.val < self.target:
                return dfs(node.right)
            else:
                return dfs(node.left)
        
        return dfs(root)



class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)