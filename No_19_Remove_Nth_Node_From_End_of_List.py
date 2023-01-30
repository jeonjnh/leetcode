"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead = head
        cnt = 0
        while(dummyHead):
            cnt += 1
            dummyHead = dummyHead.next

        if(cnt == 1):
            return None

        dummyHead = head
        deleteNode = cnt - n
        cnt = 0
        
        while(dummyHead):
            if(deleteNode-1 == cnt):
                dummyHead.next = dummyHead.next.next
            if(deleteNode-1 < 0):
                dummyHead = dummyHead.next
                return dummyHead
            dummyHead = dummyHead.next
            cnt += 1


        return head
