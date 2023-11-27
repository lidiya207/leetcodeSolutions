class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightsum=sum(nums)
        leftsum=0
        output=[]
        for i in nums:
                output.append(abs(rightsum-leftsum-i))
                rightsum-=i
                leftsum+=i
        return output       
                