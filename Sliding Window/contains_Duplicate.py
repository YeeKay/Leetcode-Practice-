# Problem Description: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        dictionary = {}

        for index, num in enumerate(nums):
            if num in dictionary and index - dictionary[num] <= k: # if num exists as dictionary keys 
                return True

            dictionary[num] = index # dictionary value is the indices 
        
        return False

# Input: nums = [1,2,3,1], k = 3
# Output: true

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false