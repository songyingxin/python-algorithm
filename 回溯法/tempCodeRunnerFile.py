class Solution:
#     def generateParenthesis(self, n):

#         result = []
#         item = []
#         left_num = 0
#         right_num = 0

#         self.back_track(n*2, item, left_num, right_num, result)

#         return result
    
#     def  back_track(self, n, item, left_num, right_num, result):
#         """
#         left_num : 左括号数量
#         right_num: 右括号数量
#         """

#         if n == 0:
#             if left_num == right_num:
#                 result.append(''.join(item))
#             return

#         left_item = item.copy()
#         left_item.append('(')
#         self.back_track(n-1, left_item, left_num+1, right_num, result)

#         if left_num > right_num:
#             right_item = item.copy()
#             right_item.append(')')
#             self.back_track(n-1, right_item, left_num, right_num+1, result)