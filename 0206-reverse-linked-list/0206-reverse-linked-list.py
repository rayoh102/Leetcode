# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # prev stores the previous node 
        # curr stores the current node, which is the head
        prev, curr = None, head

        while curr:
            # Temporarily store next node in temp
            temp = curr.next
            
            # Reverse the "next" pointer to point to prev
            curr.next = prev
            
            # Update the current and previous nodes
            prev = curr
            curr = temp
        return prev
        