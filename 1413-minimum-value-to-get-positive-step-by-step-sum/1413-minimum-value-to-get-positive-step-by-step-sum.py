class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = float('inf') 

        current_sum = 0
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)

        return max(1, 1 - min_sum)

