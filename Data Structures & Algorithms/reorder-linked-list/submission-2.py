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
        for i in range(1,length):
            q.next=info[length-i]
            q=q.next
            if length-i==i:
                q.next=None
                break
            q.next=info[i]
            q=q.next
            if i+1==length-i:       
                q.next=None
                break

            

        

        
        