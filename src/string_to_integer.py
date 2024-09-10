'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example:
Input: s = " -042"
Output: -42

Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)            ^
Step 2: "   -042" ('-' is read, so the result should be negative)             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
'''


import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        while s[0] == ' ':
            s = s[1:]
            if len(s) == 0:
                return 0

        p = re.compile(r'([-+]{0,1}[\d]+)')
        for m in p.finditer(s):
            if m.start() == 0:
                if int(m.group()) >= 2**31:
                    return 2147483647
                elif int(m.group()) <= -2**31:
                    return -2147483648
                else:
                    return int(m.group())
            break

        return 0

if __name__ == '__main__':
    s = " "
    print(Solution().myAtoi(s))

