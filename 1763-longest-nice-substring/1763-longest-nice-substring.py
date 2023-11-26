class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
           
            return all(c.swapcase() in sub for c in sub)

        result = ""
        n = len(s)

       
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(result):
                    result = substring

        return result
