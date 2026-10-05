class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        list = []

        temp = head

        while temp != None:
            list.append(temp.val)
            temp = temp.next

        temp = head

        for i in range(len(list) - 1, -1, -1):
            temp.val = list[i]
            temp = temp.next

        return head