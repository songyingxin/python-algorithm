
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []

        while queue:
            tmp_queue = []
            tmp = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                
                if node.right:
                    tmp_queue.append(node.right)

            queue = tmp_queue
            res.append(tmp)
        
        return res


