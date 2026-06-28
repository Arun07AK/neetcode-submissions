# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p=head
        q=None
        while p is not None :
            next_adres=p.next
            p.next=q
            q=p
            p=next_adres
        return q
            
        
        
            
        
        

        