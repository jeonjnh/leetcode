# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummyHead = ListNode()
        ptr = dummyHead

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
            else:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next

        if(list1):
            ptr.next = list1

        if(list2):
            ptr.next = list2
        
        return dummyHead.next
