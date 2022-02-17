class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        queue = [[0, root]]
        max_wide = 0

        while queue:
            max_wide = max(max_wide, queue[-1][0] - queue[0][0] + 1)
            tmp = []

            for i, q in queue:
                if q.left:
                    tmp += [[i*2, q.left]]
                
                if q.right:
                    tmp += [[i*2+1, q.right]]
                
            queue = tmp
        
        return max_wide
