# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        p=head
        while p:
            length+=1
            p=p.next
        #dummy points to the head
        dummy=ListNode(0,head)
        p=dummy
        index=length-n+1
        q=None
        for i in range(index):
            q=p
            p=p.next
        q.next=p.next 
        #return the new head (dummy.next handes if the original head was removed)
        return dummy.next


        
        
        
            
