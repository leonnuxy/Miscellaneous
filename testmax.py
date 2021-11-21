# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:                      # if l1 is None, return l2
            return l2                   # return l2
        if not l2:                      # if l2 is None, return l1
            return l1                   # return l1
        
        carry = 0                       # carry is 0
        root = ListNode(0)          # root is a ListNode with value 0
        curr = root
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return root.next