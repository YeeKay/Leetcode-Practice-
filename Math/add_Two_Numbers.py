# Problem Description: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        carry = 0
        root = n = ListNode(0) # placeholder, keeps the code simple 

        while l1 or l2 or carry: 
            if l1:
                carry += l1.val
                l1 = l1.next # iterates through the linked list
            
            if l2:
                carry += l2.val
                l2 = l2.next # iterates through the linked list
            
            carry, val = carry // 10, carry % 10  # div mod 

            n.next = n = ListNode(val) # update pointer in the linked list 
        
        return root.next 
    
# Time complexity: O(n)
# Space complexity: O(n)