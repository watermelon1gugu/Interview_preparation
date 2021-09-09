# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getKthFromEnd(self, head, k: int):
        n = 1
        temp = head
        while temp.next is not None:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n):
            if i == n - k:
                return temp
            temp = temp.next
