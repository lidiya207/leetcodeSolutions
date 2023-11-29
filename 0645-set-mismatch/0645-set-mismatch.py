class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = None
        missing = None
        
        num_counter = Counter(nums)
        
        for i in range(1, len(nums) + 1):
            if i not in num_counter:
                missing = i
            if num_counter[i] > 1:
                duplicate = i
        
        return [duplicate, missing]
