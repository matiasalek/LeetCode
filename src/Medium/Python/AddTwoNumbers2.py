# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        aux = l1
        first_number = []

        aux2 = l2
        second_number = []

        while aux != None:
            first_number.append(aux.val)
            aux = aux.next
        first_number_in_order = first_number[::-1]

        while aux2 != None:
            second_number.append(aux2.val)
            aux2 = aux2.next
        second_number_in_order = second_number[::-1]

        first_number_result = 0
        second_number_result = 0

        for digit in first_number_in_order:
            first_number_result = first_number_result * 10 + digit

        for digit in second_number_in_order:
            second_number_result = second_number_result * 10 + digit
        
        third_number = first_number_result + second_number_result
        third_number_list = list(map(int, str(third_number)))
        third_number_list_to_linked_list = third_number_list[::-1]
        
        dummy = ListNode()
        current = dummy

        for digit in third_number_list_to_linked_list:
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
