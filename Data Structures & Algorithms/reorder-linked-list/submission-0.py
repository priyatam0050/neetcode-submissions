# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        k=[]
        current=head
        while current:
            k.append(current)
            current=current.next
        
        l=0
        r=len(k)-1
        res=k[0]
        l+=1
        while l<r:
            
            res.next=k[r]
            res.next.next=k[l]
            res=res.next.next
            l+=1
            r-=1
        res=k[r]
        res.next=None
        temp1=head
        while temp1:
            temp1=temp1.next
        return temp1
        