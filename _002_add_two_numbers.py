"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p, q, curr, carry = l1, l2, dummyHead, 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = int(sum / 10)  # 无进位(<1)时为0，有进位(>1)为1
            curr.next = ListNode(sum % 10)
            curr = curr.next    # 走链
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:   # 循环结束，如果还有进位
            curr.next = ListNode(carry)
        return dummyHead.next


s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
r = s.addTwoNumbers(l1, l2)
print([r.val, r.next.val, r.next.next.val])
