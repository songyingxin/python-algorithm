class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []
        def dfs(node, str_val):
            if not node:
                return 

            if str_val == '':
                str_val = str(node.val)
            else:
                str_val = str_val + '->' + str(node.val)

            if not node.left and not node.right:
                res.append(str_val)
                return 
        
            dfs(node.left, str_val)
            dfs(node.right, str_val)
        
        dfs(root, '')

        return res
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def binary(root, item):
            if not root:
                return 

            item.append(str(root.val))
          
            if not root.left and not root.right:
                res.append('->'.join(item))
                return
        
            binary(root.left, item[:])
            binary(root.right, item[:])
            
        binary(root, [])
        return res
        