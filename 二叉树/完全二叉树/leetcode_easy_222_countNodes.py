class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        # 求左子树高度
        left_height = 0
        node = root
        while node:
            node = node.left 
            left_height += 1

        # 求右子树高度
        right_height = 0
        node = root
        while node:
            node = node.right
            right_height += 1
        
        if left_height == right_height:
            return 2**left_height - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
