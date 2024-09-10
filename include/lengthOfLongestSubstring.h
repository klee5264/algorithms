//
// Created by K on 8/19/2024.
//


#ifndef TEST_H
#define TEST_H

#include <unordered_set>
#include <string>

using namespace std;

// namespace lols {
class LengthOfLongestSubstring {
public:
    int solution(string s) {
        int n = s.length();
        int maxLength = 0;
        unordered_set<char> charSet;
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (charSet.count(s[right]) == 0) {
                charSet.insert(s[right]);
                maxLength = max(maxLength, right - left + 1);
            } else {
                while (charSet.count(s[right])) {
                    charSet.erase(s[left]);
                    left++;
                }
                charSet.insert(s[right]);
            }
        }

        return maxLength;
    }
};

// }

#endif //TEST_H
