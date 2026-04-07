class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            tmp = []
            new_stack = []
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            res.append(tmp)
            stack = new_stack
        
        return res


        