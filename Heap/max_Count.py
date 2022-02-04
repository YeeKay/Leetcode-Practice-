# Problem Description:
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


class Solution:
    def maxProduct(self, nums: [int]) -> int:
        first, second = 0, 0

        for num in nums:
            if num > first: 
                first, second = num, first
            
            elif num > second:
                second = num
        
        return (first - 1) * (second - 1)


# Input: nums = [3,4,5,2]
# Output: 12 

# Input: nums = [1,5,4,5]
# Output: 16

# Input: nums = [3,7]
# Output: 12

# Time complexity: O(N)
# Space complexity: O(1)