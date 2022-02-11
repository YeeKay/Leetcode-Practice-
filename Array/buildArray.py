# Problem Description: 
# Given a zero-based permutation nums (0-indexed),  build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        
        # turn the array into a=qb+r
        for i in range(len(nums)):
            r = nums[i]
            
            # retrieve correct value from potentially already processed element
            # i.e. get r from something maybe already in the form a = qb + r
            # if it isnt already processed (doesnt have qb yet), that's ok b/c
            # r < q, so r % q will return the same value
            b = nums[nums[i]] % q
            
            # put it all together
            nums[i] = q*b + r
            
        # extract just the final b values
        for i in range(len(nums)):
            nums[i] = nums[i] // q
        
        return nums

# Time complexity: O(n)
# Space complexity: O(1)

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans = list()

#         for index, num in enumerate(nums):
#             ans.append(nums[nums[index]])
        
#         return ans

# Time complexity: O(n)
# Space complexity: O(n)


# Input: nums = [0, 2, 1, 5, 3, 4]
# Output: [0, 1, 2, 4, 5, 3]

# Input: nums = [5, 0, 1, 2, 3, 4]
# Output: [4, 5, 0, 1, 2, 3]




