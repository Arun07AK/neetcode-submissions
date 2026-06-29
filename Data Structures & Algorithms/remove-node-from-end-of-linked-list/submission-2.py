# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        length=0
        while p:
            length+=1
            p=p.next
        p=head
        index=length-n
        q=None
        if index==0:
            head=p.next
            return head
        for i in range(index):
            q=p
            p=p.next
        q.next=p.next
        return head


        
        
        
            
