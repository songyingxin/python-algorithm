# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.visited = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.move_core(threshold, rows, cols, 0, 0)

    
    def move_core(self, threshold, rows, cols, row, col):

        if row/10 + row % 10 + col/10 + col % 10 > threshold:
            return 0
        
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        
        if (row, col) in self.visited:
            return 0
        
        self.visited[(row, col)] = 1

        return 1 + self.move_core(threshold, rows, cols, row-1, col) + self.move_core(threshold, rows, cols, row+1, col) + self.move_core(threshold, rows, cols, row, col-1) + self.move_core(threshold, rows, cols, row, col+1)


if __name__ == "__main__":
    
    print(Solution().movingCount(18, 10, 10))
