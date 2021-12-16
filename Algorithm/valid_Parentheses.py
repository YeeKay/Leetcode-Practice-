# Problem Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # first-in-last-out

        symbol_dict = {'(':')', 
                       '{':'}', 
                       '[':']'}

        for c in s:
            if c in symbol_dict: # if it's the starting-bracket
                stack.append(c) # append it to the stack

            else: # ending-bracket
                if stack == [] or symbol_dict[stack.pop()] != c: #  ending-bracket 
                    return False

        return stack == [] 

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false
