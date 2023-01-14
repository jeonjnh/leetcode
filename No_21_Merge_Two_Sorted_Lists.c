/*
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){

    struct ListNode dummyHead;
    dummyHead.next = NULL;
    struct ListNode *merge = &dummyHead;

    if(list1 == NULL && list2 == NULL) {return NULL;}

    while(list1 && list2){
        if(list1->val < list2->val){
            merge->next = list1;
            list1 = list1->next;
            merge = merge->next;
        }
        else{
            merge->next = list2;
            list2 = list2->next;
            merge = merge->next;
        }
    }

    if(list1){
        merge->next = list1;
    }
    if(list2){
        merge->next = list2;
    }

    return dummyHead.next;

}
