class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 1:
            return True

        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1
