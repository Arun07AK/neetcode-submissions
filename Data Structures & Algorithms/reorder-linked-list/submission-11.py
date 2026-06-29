# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=head
        fast=head
        slow=head
        #slow and fast pointers to split the list
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #slow pointer points the middle node and slow.next points the start of the 2nd half
        curr=slow.next
        slow.next=None
        q=None
        #reversing the 2nd half
        while curr:
            nxt=curr.next
            curr.next=q
            q=curr
            curr=nxt
        #q is the head of the 2nd half and p is the head of first half
        #now we merge alternatively
        p1=p
        p2=q
        while p2:
            nxt1=p1.next
            nxt2=p2.next
            p1.next=p2
            p2.next=nxt1
            p1=nxt1
            p2=nxt2


