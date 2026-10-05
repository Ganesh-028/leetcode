# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        temp = head
        x=[]
        while temp != None:
            x.append(temp.val)
            temp = temp.next
        if x == x[::-1]:
            return True
        else:
            return False

        