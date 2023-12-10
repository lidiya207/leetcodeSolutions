class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to make adjacent elements closer in value
        min_difference = float('inf')

        for i in range(len(nums) - k + 1):
            current_difference = nums[i + k - 1] - nums[i]
            min_difference = min(min_difference, current_difference)

        return min_difference
