


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            
            node = TreeNode(node1.val+node2.val)
            node.left = dfs(node1.left, node2.left)
            node.right = dfs(node1.right,node2.right)

            return node
        
        return dfs(root1, root2)