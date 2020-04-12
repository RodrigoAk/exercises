'''
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        if(l1.next is None and l2.next is None):
            if(l1.val + l2.val + c < 10):
                return ListNode(l1.val + l2.val + c)
            else:
                l_sum = ListNode(l1.val + l2.val + c - 10)
                c = 1
                l_sum.next = ListNode(c)
                return l_sum
        else:
            if(l1.val + l2.val + c < 10):
                l_sum = ListNode(l1.val + l2.val + c)
                c = 0
            else:
                l_sum = ListNode(l1.val + l2.val + c - 10)
                c = 1
            l_sum.next = self.addTwoNumbers(l1.next, l2.next, c)

        return l_sum


def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
    # 7 0 8


if __name__ == "__main__":
    main()
