# Problem Description:

# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum('+' in s or -1 for s in operations)
    
# Time complexity: O(n)
# Space complexity: O(1)

# Input: operations = ["--X","X++","X++"]
# Output: 1

# Input: operations = ["++X","++X","X++"]
# Output: 3

# Input: operations = ["X++","++X","--X","X--"]
# Output: 0

# Constraints: 
# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".
    