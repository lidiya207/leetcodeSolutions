class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        result = [None] * len(words)

        for word in words:
            index = int(word[-1]) - 1
            result[index] = word[:-1]

        return " ".join(result)
