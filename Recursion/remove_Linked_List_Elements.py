# Problem Description: Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1) # dummy variable to address edge case
        dummy_head.next = head

        current_node = dummy_head
        
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next # skip the node with the value 
            else:
                current_node = current_node.next # keeps the node

        return dummy_head.next # return actual head

# Input: head = [1, 2, 6, 6, 4, 5, 6], val = 6
# Output: [1, 2, 3, 4, 5]

# Input: head = [], val = 1
# Output: []

# Input: head = [7, 7, 7, 7], val = 7
# Output: []

# Time complexity: O(n)
# Space complexity: O(1)    