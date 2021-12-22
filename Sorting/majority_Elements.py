class Solution:
    # fastest
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2] # majority element must be at the middle position
    
    # slowest - use a dictionary to keep track of the element and the number of its occurences
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

            if dictionary[num] > len(nums) // 2:
                return num
    
    # Boye-Moore Majority Vote Algorithm - number of occurences of majority elements must be more than the minority elements, thus the counter is positive. 
    def majorityElement(self, nums: List[int]) -> int:
        current_candidate, counter = nums[0], 0
        
        for num in nums:
            if num == current_candidate: 
                counter += 1 
            
            elif not counter:
                candidate, current_candidate = 1, num
            
            else:
                counter -= 1
        
        return current_candidate
        
            
    # Time complexity: O(n) - linear time complexity
    # Space complexity: O(1)

# Input: nums = [3, 2, 3]
# Output: 3

# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2 

