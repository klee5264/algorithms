from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_count = len(set(s))
        string_len = len(s)
        if string_len == unique_count:
            return string_len

        max_len = 0
        appeared_dict = defaultdict(lambda: -1)
        left_idx = 0

        for right_idx in range(string_len):
            c = s[right_idx]
            if appeared_dict[c] >= left_idx:
                left_idx = appeared_dict[c] + 1
            appeared_dict[c] = right_idx

            max_len = max(max_len, right_idx - left_idx + 1)

            if max_len == unique_count:
                break
            if string_len - left_idx <= max_len:
                break

        return max_len


if __name__ == '__main__':
    s = 'aaabbccdefgfff'
    print(Solution().lengthOfLongestSubstring(s))