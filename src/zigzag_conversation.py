import itertools

from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_dict = defaultdict(str)
        idx_list = list(range(numRows))
        idx_list += idx_list[::-1][1:-1]

        string_idx = 0
        for idx in itertools.cycle(idx_list):
            if string_idx == len(s):
                break
            row_dict[idx] += s[string_idx]
            string_idx += 1

        answer = ''
        for key in row_dict:
            answer += row_dict[key]

        return answer


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 11
    result =  "PAHNAPLSIIGYIR"  # PIARYPALISHGIN PAYPALISGHNIIR
    '''
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    '''
    '''
    P   A   H   N
    A P L S I I G
    Y   I   R
    '''
    solution = Solution()
    print(solution.convert(s, numRows))
