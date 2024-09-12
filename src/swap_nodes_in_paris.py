'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''


import re
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        a_list = [head.val]
        while ll.next:
            a_list.append(ll.next.val)
            ll = ll.next
        return a_list


        a_ll = Solution().ll_to_list(head)
        answer_list = []
        prev_val = None
        for idx, a_value in enumerate(a_ll):
            if idx % 2 - 1 == 0 and idx > 0:
                answer_list += [a_value, prev_val]
                prev_val = None
            else:
                prev_val = a_value

        if prev_val != None:
            answer_list.append(prev_val)

        return self.list_to_ll(answer_list)

    def ll_to_list(self, ll):
        if not ll:
            return []

        a_list = [ll.val]
        while ll.next:
            a_list.append(ll.next.val)
            ll = ll.next
        return a_list

    def list_to_ll(self, a_list):
        last_node = None
        while a_list:
            current_node = ListNode(val=a_list.pop(-1))
            if last_node:
                current_node.next = last_node
            last_node = current_node
        return last_node


if __name__ == '__main__':
    a_list = [2,2,0]
    a_ll = Solution().list_to_ll(a_list)
    output_ll = Solution().swapPairs(a_ll)
    output_list = Solution().ll_to_list(output_ll)
    print(output_list)
