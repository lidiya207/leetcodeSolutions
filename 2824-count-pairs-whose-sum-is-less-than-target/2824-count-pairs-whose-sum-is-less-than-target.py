from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        N = len(nums)  
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] < target:
                    count += 1

        return count
