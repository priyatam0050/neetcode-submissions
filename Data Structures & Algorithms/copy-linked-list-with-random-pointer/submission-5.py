"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       
        k2={}
        dummy =Node(0)
        head1=dummy
        current=head
        while current:
            
                
            temp1=Node(current.val)
            k2[current]=temp1
           
            dummy.next=temp1
            dummy=dummy.next    
            current=current.next
        dummy.next=None
        temp2=head
        while temp2:
            if temp2.random:
                temp2_new=k2[temp2]
                temp2_new.random=k2[temp2.random]
            temp2=temp2.next
        

        

        

        """
        final=head
        final1=head1.next
        while final:
            if final.random and final.random in k:
                ind=k.index(final.random)
               
                final1.random=k1[ind]
            final=final.next
            final1=final1.next"""
        
        return head1.next
        