class Solution:
    def isRectangleCover(self, rectangles):
        if not rectangles:
            return False
        x1 = float('inf')
        x2 = float('-inf')
        y1 = float('inf')
        y2 = float('-inf')

        nums = set()
        area = 0   # 面积
        for rect in rectangles:
            x1 = min(rect[0], x1)
            y1 = min(rect[1], y1)

            x2 = max(rect[2], x2)
            y2 = max(rect[3], y2)

            area += (rect[2] - rect[0]) * (rect[3] - rect[1])

            coord = self.get_coords(rect)
            for val in coord:
                if val not in nums:
                    nums.add(val)
                else:
                    nums.discard(val)

        # 判断是否为完美矩形：
        if (x1, y1) not in nums:   # 左下角
            return False
        if (x1, y2) not in nums:   # 左上角
            return False
        if (x2, y1) not in nums:   # 右下角
            return False
        if (x2, y2) not in nums:    # 右上角
            return False
        if len(nums) != 4:
            return False
        
        return area == (x2-x1) * (y2-y1)   # 面积对比 ， 避免重叠
    
    def get_coords(self, arr):
        start_down = (arr[0], arr[1])   # 左下角
        start_up = (arr[0], arr[3])   # 左上角
        end_down =  (arr[2], arr[1])   #  右下角
        end_up = (arr[2], arr[3])   # 右上角
    
        return [start_down, start_up, end_down, end_up]


rectangles = [[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]


print(Solution().isRectangleCover(rectangles))
