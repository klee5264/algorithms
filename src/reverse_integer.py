'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321
'''


class Solution(object):
    def reverse(self, x):
        if str(x)[0] == '-':
            answer = int('-' + str(x)[:0:-1])
        else:
            answer = int(str(x)[::-1])
        if answer < -2**31 or answer > 2**31-1:
            return 0
        else:
            return answer


if __name__ == '__main__':
    x = -1534236469
    print(Solution().reverse(x))