# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node inside our list to avoid adding to an empty list
        dummy = ListNode()
        # Tail of our list = our dummy node
        tail = dummy

        while list1 and list2:
            # if list1's value < list2's value, add list1's value to our list and iterate to next value of list1
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            # else list1's value > list2's value, add list2's value to our list and iterate to next value of list2
            else:
                tail.next = list2
                list2 = list2.next
            
            # Update the tail of our listnode
            tail = tail.next

        # If list1 isn't empty yet, then add the remaining values of list1 and add it to our list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next