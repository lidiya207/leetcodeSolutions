class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        st = list(s)
        left, right = 0, len(st) - 1

        while left < right:
            while left < right and st[left].lower() not in vowels:
                left += 1
            while left < right and st[right].lower() not in vowels:
                right -= 1

            # Swap vowels
            st[left], st[right] = st[right], st[left]
            left += 1
            right -= 1

        return ''.join(st)

# Example usage:
sol = Solution()
input_str = "hello"
