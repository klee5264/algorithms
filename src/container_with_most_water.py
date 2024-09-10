'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

from collections import defaultdict

from typing import List


class Solution:
    def maxArea(self, height_list: List[int]) -> int:
        area_component_dict = defaultdict(lambda: 0)
        for idx, height in height_list:
            if height > area_component_dict['left_height']:
                area_component_dict['left_height'] = height


        return 0


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = 49
    print(solution.maxArea(height))

