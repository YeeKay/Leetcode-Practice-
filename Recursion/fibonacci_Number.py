# Problem Description: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
# That is,F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

# naive recursive

# class Solution:
#     def fib(self, n : int) -> int:
#         if n == 0 or n == 1:
#             return n 
#         else:
#             return self.fib(n - 1) + self.fib(n - 2) # recursive solution


# memoized recursive, no re-calculation of a certain fibonacci number
# memo = {} 
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
#         if n - 1 not in memo:
#             memo[n - 1] =  self.fib(n - 1)  
#         if n - 2 not in memo:
#             memo[n - 2] = self.fib(n - 2)
        
#         return memo[n - 1] + memo[n - 2]

# iterative space-optimized performance

# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return n
        
#         memo = (0, 1)

#         for _ in range(2, n + 1): # iterative part 
#             memo = (memo[-1], memo[-1] + memo[-2]) # keep re-newing memo values as the code iterates

#         return memo[-1]

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.