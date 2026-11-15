# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        k=[]
        result=False
        k.append(head)
        if not head:
            return result
        head= head.next
        while head:
            if head not in k:
                k.append(head)
            else:
                return True
            head=head.next
        return result
            
        