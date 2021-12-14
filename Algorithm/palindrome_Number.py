# Problem Description:Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

# Solution 1: Recreate the number in reverse order 
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
        
#         reversedNum = 0
#         inputNum = x

#         while x > 0:
#             reversedNum = (reversedNum * 10) + x % 10
#             x //= 10

#         if reversedNum == inputNum:
#             return True
        
#         else:
#             return False 

# Solution 2: Recreate the number in reverse order and terminates when the number is halfway reversed
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0  and x % 10 == 0): # if x is negative, return False. if x is positive and last digit is 0, that also cannnot form a palindrome.
            return False
        
        reversedNum = 0
        inputNum = x
        
        while x > reversedNum:
            reversedNum = (reversedNum * 10) + x % 10
            x //= 10

        return True if (x == result) or (x == reversedNum // 10) else False
        

# Input: x = 121
# Output: true

# Input: x = -121
# Output: false

# Input: x = 10
# Output: false

# Input: x = -101
# Output: false