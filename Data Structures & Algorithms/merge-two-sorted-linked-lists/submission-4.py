# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        dummy=ListNode()
        curr=dummy
        while p and q :
            if p.val<q.val:
                curr.next=p
                p=p.next
            else :
                curr.next=q
                q=q.next
            curr=curr.next
        if p:
            curr.next=p
        elif q:
            curr.next=q

        return dummy.next

        
        

