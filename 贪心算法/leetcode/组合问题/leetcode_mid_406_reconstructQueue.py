class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        res = []
        for val in people:

            res.insert(val[1], val)

        return res
