



class Solution:
    def __init__(self):
        self.path_num = 0
         
    def DFS(self, root, sum):
        if not root:
            return
        sum -= root.val
        if sum == 0:
            self.path_num += 1
        self.DFS(root.left, sum)
        self.DFS(root.right, sum)
    def FindPath(self , root: TreeNode, sum: int) -> int:
        # write code here
        if not root: 
            return 0
        self.DFS(root, sum)
        self.FindPath(root.left, sum)
        self.FindPath(root.right, sum)
        return self.path_num