'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''


import itertools
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num_list = self.list_node_to_list(head)
        del num_list[-n]
        return self.list_to_list_node(num_list)

    def list_to_list_node(self, num_list):
        last_node = None
        list_node = ListNode(val='')

        for num in num_list[::-1]:
            list_node = ListNode(val=num, next=last_node)
            last_node = list_node
        return list_node

    def list_node_to_list(self, list_node):
        num_list = []
        while 1:
            num_list.append(list_node.val)
            if not list_node.next:
                break
            else:
                list_node = list_node.next
        return num_list

    def print_result(self, list_node):
        while list_node.val:
            print(list_node.val, end='')
            list_node = list_node.next
            if not list_node:
                break


if __name__ == '__main__':
    head = [3,7,9,3,5,8,0]

    head = Solution().list_to_list_node(head)
    n = 1
    # output[3, 9, 3, 5, 8, 0]
    # expected[3, 7, 9, 3, 5, 8]

    output = Solution().removeNthFromEnd(head, n)
    Solution().print_result(output)
    print(output)