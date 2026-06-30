# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_list=[]
        for head in lists:
            q=head
            while q:
                my_list.append(q.val)
                q=q.next
        my_list.sort()
        dummy=ListNode(0)
        q=dummy
        for i in range(len(my_list)):
            q.next=ListNode(my_list[i])
            q=q.next
        
        return dummy.next

            

