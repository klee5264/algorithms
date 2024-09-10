/*
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

*/

#ifndef STRINGTOINTEGER_H
#define STRINGTOINTEGER_H

#include <string>

class StringToInteger {
public:
    int solution(string s) {
        long ans = 0;
        int sign = 1;
        int i = 0;

        while (s[i] == ' ') i++;

        if (s[i] == '-' || s[i] == '+') {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
        while (i < s.length() && isdigit(s[i])) {
            ans = ans * 10 + (s[i] - '0');
            if (ans*sign <= INT_MIN) return INT_MIN;
            if (ans*sign >= INT_MAX) return INT_MAX;
            i++;
        }
        return ans * sign;
    }
};

#endif //STRINGTOINTEGER_H
