# Problem Description: Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        return haystack.index(needle)

# class Solution: 
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(haystack) < len(needle): # haystack is shorter than needle 
#             return -1

#         if not needle: # return 0 if needle == ""
#             return 0 

#         haystack_index, needle_head, needle_tail = 0, 0, len(needle) - 1
        
#         while haystack_index + needle_tail < len(haystack): 
#             if needle_head > needle_tail:
#                 return haystack_index

#             if haystack[haystack_index + needle_tail] != needle[needle_tail] or haystack[haystack_index + needle_head] != needle[needle_head]: # not substring
#                 # reset needle head and tail and move haystack pointer 1 to the right
#                 needle_head = 0 
#                 needle_tail = len(needle) - 1
#                 haystack_index += 1
        
#             elif haystack[haystack_index + needle_tail] == needle[needle_tail] and haystack[haystack_index + needle_head] == needle[needle_head]: # continue check whether the string matches
#                 needle_head += 1
#                 needle_tail -= 1
        
        # return -1

# Input: haystack = "hello", needle = "ll"
# Output: 2 

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1 

# Input: haystack =  "", needle = ""
# Output: 0
            