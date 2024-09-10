'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_int = self.ll_to_int(l1)
        l2_int = self.ll_to_int(l2)
        two_sum_list = list(str(l1_int + l2_int))[::-1]
        return self.list_to_ll(two_sum_list)

    def ll_to_int(self, ll):
        a_number_str = str(ll.val)
        while ll.next:
            a_number_str += str(ll.next.val)
            ll = ll.next
        return int(a_number_str[::-1])

    def list_to_ll(self, a_list):
        last_node = None
        while a_list:
            current_node = ListNode(val=a_list.pop(-1))
            if last_node:
                current_node.next = last_node
            last_node = current_node
        return last_node



if __name__ == '__main__':
    solution = Solution()

    a_ll = solution.list_to_ll([2,4,3])

    a = solution.list_to_ll([2,4,3])
    b = solution.list_to_ll([5,6,4])

    sol_ll = solution.addTwoNumbers(a,b)
    print(solution.ll_to_int(sol_ll))

    a_number_str = str(sol_ll.val)
    while sol_ll.next:
        a_number_str += str(sol_ll.next.val)
        sol_ll = sol_ll.next
    print(a_number_str)
