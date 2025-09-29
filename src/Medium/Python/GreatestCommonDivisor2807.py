# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        aux = head
        while aux.next:
            gcd_node = ListNode(math.gcd(aux.val, aux.next.val), aux.next)
            aux.next = gcd_node
            aux = gcd_node.next
        
        return head
