

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here

        first_index = self._get_the_first(data, 0, len(data) - 1, k)
        end_index = self._get_the_end(data, 0, len(data) - 1, k)

        if first_index > -1 and end_index > -1:
            return end_index - first_index + 1
        else:
            return 0
    
    def _get_the_first(self, data, start, end, k):

        if start > end:
            return -1

        mid = (start + end) // 2

        if data[mid] == k:
            if (mid > 0 and data[mid - 1] != k) or mid == 0:
                return mid
            else:
                end = mid -1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
        
        return self._get_the_first(data, start, end, k)

    def _get_the_end(self, data, start, end, k):
        if start > end:
            return -1

        mid = (start + end) // 2

        if data[mid] == k:
            if (mid < len(data) - 1 and data[mid+1] != k) or mid == len(data)-1:
                return mid
            else:
                start = mid + 1
        elif data[mid] > k:
            end = mid -1
        else:
            start = mid + 1
        
        return self._get_the_end(data, start, end, k)

            

if __name__ == "__main__":
    
    data = [3, 3, 3, 3, 4, 5]

    k = 3

    Solution().GetNumberOfK(data, k)


