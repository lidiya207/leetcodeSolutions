class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Initialize variables
        running_sum = 0
        result = []

        # Iterate through the elements of the input list
        for num in nums:
            # Update the running sum by adding the current element
            running_sum += num
            # Append the running sum to the result list
            result.append(running_sum)

        # Return the final result, which is the list of running sums
        return result
