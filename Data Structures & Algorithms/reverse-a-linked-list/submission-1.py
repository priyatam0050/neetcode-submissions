# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=[]
        k.append(head)
        if head:

            current=head.next
            temp1=head
            while current:
                k.append(current)
                current=current.next
           
            head=k.pop()
            
            current=head
            temp2=k.copy()
           
            j=0
            while j<len(temp2):
               
                current.next=k.pop()
                current=current.next
                j+=1
        
            current.next=None
            return head
        else:
            return head

       
       
        
        