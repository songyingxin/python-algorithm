import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)







