
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            tmp = []
            new_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            res.append(tmp)
            queue = new_queue
        
        return res[::-1]


        