# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Dummy node to make list creation easier
        dummy = ListNode(0)
        current = dummy

        # Carry from the previous addition
        carry = 0

        # Continue while there are nodes or a carry
        while l1 or l2 or carry:
            
            # Get values from the linked lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the two digits and carry
            total = val1 + val2 + carry

            # Calculate digit and new carry
            digit = total % 10
            carry = total // 10

            # Create a new node for the result
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return the actual result list
        return dummy.next