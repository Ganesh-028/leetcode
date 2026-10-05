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
        y=[]
        for i in range(len(x)-1,-1,-1):
            y.append(x[i])
        if x==y:
            return True
        else:
            return False

        