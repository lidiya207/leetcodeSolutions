class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Create a boolean array to represent the coverage
        covered = [False] * 51  # Assuming the range of numbers is from 1 to 50

        # Mark the positions covered by each range
        for start, end in ranges:
            for i in range(start, end + 1):
                if 1 <= i <= 50:  # Assuming the range of numbers is from 1 to 50
                    covered[i] = True

        # Check if all integers in the target range are covered
        for i in range(left, right + 1):
            if not covered[i]:
                return False

        return True

