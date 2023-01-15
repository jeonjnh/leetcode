/*
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){

    if(head == NULL) return NULL;
    
    struct ListNode *current = head;
    struct ListNode *back = NULL;
    struct ListNode *front = NULL;
    
    while(current != NULL) {
        front = current->next;
        current->next = back;
        back = current;
        current = front;        
    }
    
    return back;
}
