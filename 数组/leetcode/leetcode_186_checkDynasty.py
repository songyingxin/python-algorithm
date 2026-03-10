class Solution:
    def checkDynasty(self, places: List[int]) -> bool:

        repeat = set()
        max_val, min_val = 0, 14
        for place in places:
            if place == 0:
                continue
            
            max_val = max(max_val, place)
            min_val = min(min_val, place)

            if place in repeat:
                return False
            repeat.add(place)
        
        return max_val-min_val < 5