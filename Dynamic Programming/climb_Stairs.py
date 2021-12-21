# Problem Description: You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# This is essentially a Fibonacci problem 

# Memoization approach
table = {1: 1, 2: 2}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n 

        if n - 1 not in table:
            table[n - 1] = self.climbStairs(n - 1) 
        
        if n - 2 not in table:
            table[n - 2] = self.climbStairs(n - 2)
  
        table[n] = table[n - 1] + table[n - 2]

        return table[n]

# Input: 2 
# Output: 2

# Input: 3
# Output: 3