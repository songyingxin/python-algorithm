

# 递归法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root


# 迭代法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        now_node = TreeNode(val)

        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = now_node
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = now_node
                    break
                else:
                    node = node.right

        return root    