class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for x in range(len(hours)):
            if hours[x] >= target:
                ans += 1
        return ans
