class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ''
        for idx, char in enumerate(s):
            pal_list = []
            if idx == 0:
                max_pal = char
                continue
            if s[idx-1] == s[idx]:
                pal = s[idx-1] + s[idx]
                pal_type = 'even'
                pal = self.lengthen_pal(pal, idx, s, type=pal_type)
                pal_list.append(pal)

            if idx+1 <= len(s)-1:
                if s[idx-1] == s[idx+1]:
                    pal = s[idx-1] + s[idx] + s[idx+1]
                    pal_type = 'odd'
                    pal = self.lengthen_pal(pal, idx, s, type=pal_type)
                    pal_list.append(pal)

            if not pal_list:
                continue

            if len(max(pal_list)) > len(max_pal):
                max_pal = max(pal_list)

            if len(max_pal) >= 2*(len(s)-idx)-1:
                break

        return max_pal

    def lengthen_pal(self, pal, idx, s, type=''):
        increment = 1
        if type == 'even':
            while idx - (increment+1) >= 0 and idx + increment <= len(s)-1:
                if s[idx - (increment+1)] != s[idx + increment]:
                    break
                pal = f'{s[idx - (increment+1)]}{pal}{s[idx + increment]}'
                increment += 1
        elif type == 'odd':
            while idx - (increment+1) >= 0 and idx + increment + 1 <= len(s)-1:
                if s[idx - (increment+1)] != s[idx + increment + 1]:
                    break
                pal = f'{s[idx - (increment+1)]}{pal}{s[idx + increment + 1]}'
                increment += 1

        return pal


if __name__ == '__main__':
    solution = Solution()
    string = 'cccc'
    print(solution.longestPalindrome(string))

