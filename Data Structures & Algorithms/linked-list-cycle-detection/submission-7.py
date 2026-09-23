# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False

        anotherHead = head

        while head.next != None and anotherHead.next != None:
            head = head.next
            anotherHead = anotherHead.next
            
            if anotherHead is None:
                return True
            else:
                anotherHead = anotherHead.next
                if anotherHead is None: return False

            if head == anotherHead:
                return True

        return False