# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeTwoLists(self,head1,head2):
        p1=head1
        p2=head2
        dummy=ListNode(0,None)
        p=dummy
        while p1 and p2:
            if p1.val<=p2.val:
                p.next=p1
                p=p.next
                p1=p1.next
            else:
                p.next=p2
                p=p.next
                p2=p2.next
        p.next=p1 or p2

        return dummy.next
    
    def dvd_and_c(self,lists,start,end):
        if start==end:
            return lists[start]
        mid=(start+end) //2
        left=self.dvd_and_c(lists,start,mid)
        right=self.dvd_and_c(lists,mid+1,end)
        return self.mergeTwoLists(left,right)
                

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return None
        return self.dvd_and_c(lists,0,len(lists)-1)
            

            

