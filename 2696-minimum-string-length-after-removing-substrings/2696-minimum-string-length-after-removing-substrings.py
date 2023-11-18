class Solution:
    def minLength(self, s: str) -> int:
       
        stack=[] 
        for c in s:
            stack.append(c)
            if len(stack)>1:
                if"".join(stack[-2:])in ['AB' ,'CD']:
                        stack.pop()
                        stack.pop()
        return len(stack)     