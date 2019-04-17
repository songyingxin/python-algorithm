class Solution:
    def combine(self, n, k):
        result = []
        item = []
        self.back_track(n, k, item, result)
        return result
    
    def back_track(self, n, k, item, result):
        if k == 0:
            result.append(item)

        start = 1 if not item else item[-1]+1
        for val in range(start, n+1):
            new_item = item.copy()
            new_item.append(val)
            self.back_track(n, k-1, new_item, result)
    
if __name__ == "__main__":
    n = 4
    k = 2

    print(Solution().combine(n, k))
