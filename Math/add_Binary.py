# Problem Description: Given two binary strings a and b, return their sum as a binary string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop()) # start arithmetic from least significant digit
            
            if b:
                carry += int(b.pop()) 
            
            result = carry % 2 + result # append "0" or "1" to resulting answer string 
            carry //= 2 # calculate carry   

        return result 

# Input: a = "11", b = "1"
# Output: 100

# Input: a = "1010", b = "1011"
# Output: "10101"