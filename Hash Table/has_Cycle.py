# Problem Description: 
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next 

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        
            return True   # when slow catches up on fast, that means there must be a cycle in the linked list 
            
        except:
            return False 

# Input: head = [3, 2, 0, -4], pos = 1
# Output: true

# Input: head = [1, 2], pos = 0
# Output: true

# Input: head = [1], pos = -1
# Output: false

# Time complexity: O(n)
# Space complexity: O(1)

        