class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        total_sum = 0

        # Calculate the prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        # Calculate the sum of all odd-length subarrays
        for i in range(n):
            for j in range(i, n, 2):
                total_sum += prefix_sum[j + 1] - prefix_sum[i]

        return total_sum
