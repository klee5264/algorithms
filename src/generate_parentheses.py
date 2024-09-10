'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 1
Output: ["()"]
Input: n = 2
Output: ["()()", "(())"]
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Input: n = 4
Output: ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
Mine:   ['(((())))','((()()))','((())())','((()))()','(()(()))','(()()())','(()())()',          ,'(())()()','()((())),'()(()())','()(())()','()()(())','()()()()']

'''


import re
from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        elif n == 2:
            return ['()()', '(())']
        else:
            result_list = []
            for prev_result in self.generateParenthesis(n-1):
                p = re.compile("\(\)")
                for m in p.finditer(prev_result):
                    for element in ['()()', '(())']:
                        result_list.append(prev_result[:m.start()] + element + prev_result[m.start()+2:])

            return list(set(result_list))


if __name__ == '__main__':
    n = 4
    output = Solution().generateParenthesis(n)
    print(len(output), output)
