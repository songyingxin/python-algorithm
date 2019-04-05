class Solution:
    def combinationSum(self, candidates, target):
        result = []
        item = []
        candidates = sorted(candidates)
        self.back_track(candidates, target, item, result)
        return result
    
    def back_track(self, candidates, target, item, result):

        if target <= 0:
            if target == 0:
                result.append(item)
            return
        start = 0 if not item else candidates.index(item[-1])  # 此处是核心，避免超时
        for i in range(start, len(candidates)):
            new_item = item.copy()
            new_item.append(candidates[i])
            self.back_track(candidates, target-candidates[i], new_item, result)

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))