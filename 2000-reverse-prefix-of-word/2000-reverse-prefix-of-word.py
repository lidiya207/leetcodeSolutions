class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the target character
        idx = word.find(ch)
        
        if idx != -1:
            # Reverse the prefix substring
            word = word[:idx+1][::-1] + word[idx+1:]
        
        return word