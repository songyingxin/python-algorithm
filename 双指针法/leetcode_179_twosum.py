class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left = 0
        right = len(price) - 1

        while left < right:
            s = price[left] + price[right]
            if s == target:
                return [price[left], price[right]]
            elif s > target:
                right -= 1
            else:
                left += 1
                


        