class Solution(object):
    def lengthOfLongestSubstring(self, s):
     
        N = len(s)
        max_length = 0
        
        mapp = {}
        
        left,right = 0,0
        while right < N:
            if s[right] not in mapp:
                mapp[s[right]] = right
            else:
                
                left = max(mapp[s[right]],left)

            
            max_length = max(max_length, right - left+1)
           
            mapp[s[right]] = right +1
            right += 1
        
        return max_length