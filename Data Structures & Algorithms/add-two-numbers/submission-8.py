# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1=l1
        current2=l2
        dummy=ListNode()
        head1=dummy
        temp2=0

        while current1 or current2:
            temp=0
           
            flag=False
            
            if not current2:
                while current1:
                    temp=current1.val+temp2
                    temp1=str(temp)
                    temp1=temp1[::-1]
                    temp2=0
                    if len(temp1)>1:
                        temp2=int(temp1[1])
                        flag=True
                    print(temp1[0])
                    new_list=ListNode(temp1[0])
                    dummy.next=new_list
                    dummy=dummy.next
                    current1=current1.next
            elif not current1:
                while current2:
                    temp=current2.val+temp2
                    temp1=str(temp)
                    temp1=temp1[::-1]
                    temp2=0
                    if len(temp1)>1:
                        temp2=int(temp1[1])
                        flag=True
                    print(temp1[0])
                    new_list=ListNode(temp1[0])
                    dummy.next=new_list
                    dummy=dummy.next
                    current2=current2.next
            else:
                temp=current1.val+current2.val+temp2
                temp1=str(temp)
                temp1=temp1[::-1]
                temp2=0
                if len(temp1)>1:
                    temp2=int(temp1[1])
                    flag=True

                new_list=ListNode(temp1[0])
                dummy.next=new_list
                dummy=dummy.next

                current1=current1.next
                current2=current2.next








                
            



            

        if flag and temp2!=0:
            
            new_list=ListNode(temp2)
            dummy.next=new_list
            new_list.next=None
        else:
            dummy.next=None
        return head1.next
        
            

        