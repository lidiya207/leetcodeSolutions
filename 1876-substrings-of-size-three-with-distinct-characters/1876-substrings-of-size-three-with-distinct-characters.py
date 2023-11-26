class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result =0
        for i in range(len(s)-2):
            if s[i]!=s[i+1] and s[i+1] != s[i+2] and s[i]!=s[i+2]:
                result +=1
        return result    