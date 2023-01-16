# 206. Reverse Linked List
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        current = head
        front= ListNode()
        front = None
        back = ListNode()
        back = None
        
        while(current is not None):
            front = current.next
            current.next = back
            back = current
            current = front

        return back
