# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=[]
        if head.next is None and n==1:
            head=None
            return head
        current=head
        k.append(current)
        current=current.next
        while current:
            k.append(current)
            current=current.next
       
        temp=k[-n].next
        k[-n].next=None
        if n>=len(k):
            return temp
        if k[-n-1] is not None:
            k[-n-1].next=temp
        

        return head
        