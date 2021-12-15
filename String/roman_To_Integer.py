# Problem Description: Given a roman numeral, convert it to an integer.

# A straightforward solution
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        z = 0
        string_length = len(s)

        for i in range(0, string_length - 1):
            if symbol_dict[s[i]] < symbol_dict[s[i + 1]]: # cases such as "IV", "IX", "XL", "XC", "CD,""CM"
                z -= symbol_dict[s[i]]
            
            else:
                z += symbol_dict[s[i]] 
        
        return z + symbol_dict[s[-1]] # add the last letter 

# Input: s = "III"
# Output: 3

# Input: s = "LVIII"
# Output: 58

# Input: s = "MCMXCIV"
# Output: 1994

# Time complexity: O(n)
# Space complexity: O(1)