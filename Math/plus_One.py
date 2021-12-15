# Problem Description: You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digit = (int)("".join(map(str, digits))) # convert digits array to integer
        
        digit += 1 # plus one 
        
        return map(int, str(digit)) # convert integer back to digits array
        
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]

# Input: digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]

# Input: digits = [0]
# Output: [1]

# Input: digits = [9]
# Output: [1, 0]
