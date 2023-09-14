class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            tmp_queue = []
            res.append(queue[-1].val)
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            
            queue = tmp_queue
        
        return res




