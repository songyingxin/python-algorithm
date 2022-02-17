class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            res.append(queue[-1].val)
            tmp = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp

        return res




