class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        presum = 0
        largest_altitude = 0
        n = len(gain)
        
        for i in range(n):
            presum += gain[i]
            largest_altitude = max(largest_altitude, presum)

        return largest_altitude
