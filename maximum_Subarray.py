" Problem description : Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum."
class Solution:
    # Kadane's algorithm 
    def maxSubArray(self, nums: [int]) -> int:
        # initialization
        max_number = float("-inf")
        max_counter = 0   

        for num in nums:
            max_counter  += num
            
            if max_counter > max_number:
                max_number = max_counter

            # break the sub-array once the sum drops to 0 upon adding one element in the array
            if max_counter < 0:
                max_counter = 0 # reset to 0 to calculate the sum of a new subarray

        return max_number


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
print(sol.maxSubArray([-1, -2, -3, -4]))

# [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
# [1] -> 1
# [5, 4, -1, 7, 8] -> 23
# [-1, -2, -3, -4] -> -1 




