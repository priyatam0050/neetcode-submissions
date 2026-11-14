# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        current1=list1
        current2=list2
       

        if current1.val==current2.val:
            head=current1
            current1=current1.next
            head.next=current2
            current2=current2.next
            temp=head.next
        elif current1.val<current2.val:
            head=current1
            temp=current1
            current1=current1.next
        else:
            head=current2
            temp=current2
            current2=current2.next
       
        
 
        while current1 or current2:

          if not current1:
            while current2:
                temp.next=current2
                current2=current2.next
                temp=temp.next
          elif not current2:
            while current1:

                temp.next=current1
                current1=current1.next
                temp=temp.next

          elif current1.val==current2.val:
            temp.next=current1
            current1=current1.next
            temp.next.next=current2
            current2=current2.next
            temp=temp.next.next
            
          elif current1.val>current2.val:
                temp.next=current2
                current2=current2.next
                temp=temp.next
                
               
          else:
                temp.next=current1
                current1=current1.next
                temp=temp.next
               
                

        return head


    
        
        