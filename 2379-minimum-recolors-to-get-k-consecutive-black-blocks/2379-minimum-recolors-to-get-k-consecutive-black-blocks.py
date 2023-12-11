class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_recolors = float('inf')

        for i in range(n - k + 1):
            subsequence = blocks[i:i + k]
            recolors = k - max(subsequence.count('A'), subsequence.count('B'))
            min_recolors = min(min_recolors, recolors)

        return min_recolors

