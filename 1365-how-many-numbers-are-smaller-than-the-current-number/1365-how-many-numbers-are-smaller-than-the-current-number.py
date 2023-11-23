class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
      
       sortnums= sorted(nums)
       dic={}
       result=[]
        
       for i in range(len(sortnums)):
          if sortnums[i] not in dic:
                dic[sortnums[i]]=i
       for i in nums:
            result.append(dic[i])
       return result   