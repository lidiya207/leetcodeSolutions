class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))  # Sort by absolute values
        res = [num ** 2 for num in nums]
        return res
