# Problem description: Given an integer, convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        # A dictionary that stores symbol corresponding with their values 
        symbol_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        res = ""

        for key in symbol_dict:
            while num >= key: # check whether the number is dividable by the value 
                res += symbol_dict[key] # append the string 
                num -= key # subtracts the value by the key   
        
        return res

sol = Solution()
print(sol.intToRoman(3))
print(sol.intToRoman(4))
print(sol.intToRoman(9))
print(sol.intToRoman(58))
print(sol.intToRoman(1994))

# Input: num = 3
# Output: "III"

# Input: num = 4
# Output: "IV"

# Input: num = 9
# Output: "IX"

# Input: num = 58
# Output: "LVIII"

# Input: num = 1994
# Output: "MCMXCIV"

# Time Complexity: O(n)
# Space Complexity: O(1)