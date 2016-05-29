class Solution(object):
    def reverse(self, head):
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
