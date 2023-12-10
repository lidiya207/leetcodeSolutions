class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Check if removing the current element from the left yields a middle index
            if left_sum == total_sum - left_sum - num:
                return i
            
            left_sum += num

        # If no middle index is found
        return -1
