class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1  # Handle empty list case

        max_num = max(nums)
        max_index = nums.index(max_num)

        for i, num in enumerate(nums):
            if i != max_index and num * 2 > max_num:
                return -1  # Condition for not being dominant

        return max_index
