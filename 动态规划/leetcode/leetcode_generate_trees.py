# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        return self.build_tree(1, n)
    
    def build_tree(self, start, end):
        ans = []

        # 此时没有数字，将 None 加入结果中
        if start > end:
            ans.append(None)
            return ans

        # 只有一个数字， 当前数字作为一棵树加入结果中
        if start == end:
            tree = TreeNode(start)
            ans.add(tree)
            return ans        
        
        # 尝试以每个数字作为根节点
        for i in range(start, end+1):
            left_trees = self.build_tree(start, i-1)
            right_trees = self.build_tree(i+1, end)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    
                    ans.add(root)
        return ans





