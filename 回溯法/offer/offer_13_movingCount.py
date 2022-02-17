class Solution:
    def __init__(self):
        self.set = [] # 存放曾经到过的位置 已经计数过的位置
        
    # 计算不同位置的和
    def sum_every(self,num):
        res = 0
        while num>=10:
            res += num%10
            num = num//10
        return res + num
     
    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        # write code here
        return self.Find(threshold, rows-1, cols-1, 0, 0) # 从（0，0）点开始 向右下角寻找
     
    def Find(self, threshold, rows, cols, x, y):
        if x<0 or y<0 or x>rows or y>cols or threshold < (self.sum_every(x)+self.sum_every(y)): # 不满足边界条件直接返回0
            return 0
        if [x,y] in self.set: # 如果曾经到过这个位置，该位置已经被计数 直接返回0 跳过
            return 0
        else:
            self.set.append([x,y])
        res_x = self.Find(threshold, rows, cols, x+1, y) # 向右 x轴方向计算
        res_y = self.Find(threshold, rows, cols, x, y+1) # 向下 y轴方向计算
        return res_x + res_y +1 # 将分叉中的计算个数 加上 分叉节点的个数1