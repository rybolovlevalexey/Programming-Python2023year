# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        mid = head
        cnt = 1
        while cur.next is not None:
            cur = cur.next
            cnt += 1
            if cnt % 2 == 0:
                mid = mid.next
        return mid