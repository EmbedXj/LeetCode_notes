class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res_str = []
        if numRows == 1:
            return s
        skip_step = numRows * 2 - 2
        str_len = len(s)

        for i in range(numRows):
            for j in range(0, str_len, skip_step):
                res_str += [s[j + i]] if j + i < str_len else []
                if (i != 0) and (i != numRows -1) and (j + skip_step - i < str_len):
                    res_str += [s[j + skip_step - i]]
#                print(''.join(res_str))
        return ''.join(res_str)