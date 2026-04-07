class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == val:
            return root
<<<<<<< HEAD
        
=======
>>>>>>> aee39073896dc72ae9473a4ac3cfc60c2efb46c8
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)