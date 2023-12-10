class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        divisors_sum = 1  

        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                divisors_sum += n
                if n != num // n:
                    divisors_sum += num // n

        return divisors_sum == num
