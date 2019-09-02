# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        def helper(node):
            if not node:
                return 0, None, float('-inf'), float('inf')
            
            left_len, left_head, left_max, left_min = helper(node.left)
            right_len, right_head, right_max, right_min = helper(node.right)

            # 判断以 node 为根的树是否为搜索二叉树
            if left_head == node.left and right_head == node.right and left_max < node.val < right_min:
                result_len = left_len + right_len + 1
                result_head = node
            else:   
                result_len = max(left_len, right_len)
                result_head = left_head if left_len > right_len else right_head
        
            max_val = max(left_max, right_max, node.val)
            min_val = min(left_min, right_min, node.val)

            return result_len, result_head, max_val, min_val
        
        result, _, _, _ = helper(root)

        return result


            


