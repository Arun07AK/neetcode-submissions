# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=head
        length=0
        info={}
        index=0
        while p :
            info[index]=p
            index+=1
            length+=1
            p=p.next
        result_head=info[0]
        q=result_head
        l=1
        r=length-1
        while l<=r:
            q.next=info[r]
            q=q.next
            r-=1
            if l>r:
                break
            q.next=info[l]
            q=q.next
            l+=1
        q.next=None
        
                

            

        

        
        