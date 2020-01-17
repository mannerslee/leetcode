# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        all_items_list = []
        for p in lists:
            while p:
                all_items_list.append(p.val)
                p = p.next
        all_items_list.sort()
        head = ListNode(-1)
        p = head
        for i in all_items_list:
            p.next = ListNode(i)
            p = p.next
        return head.next

