class Solution:
    def combinationSum3(self, k, n):
        result = []
        item = []
        self.back_track(n,k, item, result)
        return result
    
    def back_track(self, n, k, item, result):

        if k == 0:
            if sum(item) == n:
                result.append(item)
            return
        
        start = 1 if not item else item[-1]+1

        for val in range(start, 10):
            new_item = item.copy()
            new_item.append(val)
            self.back_track(n, k-1, new_item, result)

if __name__ == "__main__":
    k = 3
    n = 9

    print(Solution().combinationSum3(k, n))
