# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        aux = head
        visited = set()
        
        while aux:
            if aux in visited:
                return True
            visited.add(aux)
            aux = aux.next
        return False
