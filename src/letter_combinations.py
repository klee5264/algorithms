'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

'''

from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_list = list(digits)
        int_to_letter_list_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digit_list) == 0:
            return []
        elif len(digit_list) == 1:
            return int_to_letter_list_dict[digits]

        answer_list = []
        while digit_list:
            if not answer_list:
                answer_list = int_to_letter_list_dict[digit_list.pop(0)]

            object_list = int_to_letter_list_dict[digit_list.pop(0)]

            temp_answer_list = []
            for answer_element in answer_list:
                for object_element in object_list:
                    temp_answer_list.append(answer_element+object_element)
            answer_list = temp_answer_list

        return answer_list


if __name__ == '__main__':
    input_str = '23'
    output = Solution().letterCombinations(input_str)
    print(output)