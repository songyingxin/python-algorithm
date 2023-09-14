


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.max_node = []
        self.max_count = 0

        self.pre = None
        self.now_count = 0

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if node.val == self.pre:
                self.now_count += 1
            else:
                self.now_count = 0
            
            if self.max_count < self.now_count:
                self.max_node = [node.val]
                self.max_count = self.now_count
            elif self.max_count == self.now_count:
                self.max_node.append(node.val)
            
            self.pre = node.val
            dfs(node.right)
        
        dfs(root)
        return self.max_node