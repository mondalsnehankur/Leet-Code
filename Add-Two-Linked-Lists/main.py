# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Dummy node to simplify building the result list
        dummy = ListNode()
        current = dummy

        carry = 0

        # Continue until both lists are exhausted and there is no carry
        while l1 or l2 or carry:

            # Get values from current nodes (0 if node doesn't exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum
            total = val1 + val2 + carry

            # Update carry
            carry = total // 10

            # Store the digit
            digit = total % 10

            # Create a new node and attach it
            current.next = ListNode(digit)

            # Move current pointer
            current = current.next

            # Move l1 and l2 pointers if possible
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return the head of the new linked list
        return dummy.next
