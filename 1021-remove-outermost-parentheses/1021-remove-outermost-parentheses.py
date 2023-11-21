class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        open_count = 0
        close_count = 0
        start = 0  

        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                close_count += 1

          
            if open_count == close_count:
               
                res += s[start + 1:i]
               
                start = i + 1

        return res
