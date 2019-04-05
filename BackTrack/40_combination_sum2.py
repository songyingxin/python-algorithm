class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        item = []
        candidates = sorted(candidates)
        self.back_track(candidates, target, item, result)
        return result

    def back_track(self, candidates, target, item, result):

        if target <= 0:
            if target == 0:
                if item not in result:
                    result.append(item)
            return
        if not item:
            start = 0
        else:
            index = candidates.index(item[-1]) 
            start = index + item.count(item[-1]) 
        for i in range(start, len(candidates)):
            new_item = item.copy()
            new_item.append(candidates[i])
            self.back_track(candidates, target-candidates[i], new_item, result)

if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
