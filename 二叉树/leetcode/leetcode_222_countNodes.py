class Solution:
    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        left_height = 0
        left_node = root

        right_height = 0
        right_node = root

        # 求左子树高度
        while left_node:
            left_node = left_node.left 
            left_height += 1
        
        while right_node:
            right_node = right_node.right
            right_height += 1
        
        if left_height == right_height:
            return 2**left_height - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
