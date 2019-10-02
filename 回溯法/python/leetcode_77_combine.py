class Solution:
    def combine(self, n, k):

        def dfs(t, item):
            if k == t:
                result.append(item)
                return

            start = 1 if not item else item[-1] + 1

            # 此处的end 可为 n+1， 此处进行了剪枝
            end = n+1 - (k-len(item)) + 1
            for i in range(start, end):
                new_item = item[:]
                new_item.append(i)
                dfs(t+1, new_item)

        result = []
        dfs(0, [])

        return result
