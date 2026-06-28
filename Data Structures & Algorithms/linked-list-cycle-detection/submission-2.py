# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head
        q=head
        while q and q.next:
            p=p.next
            q=q.next.next
            if p==q:
                return True
        return False
        