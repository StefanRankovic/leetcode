class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        cur = 0
        down = True
        for i, x in enumerate(s):
            rows[cur] += x
            if down:
                if cur + 1 < numRows:
                    cur += 1
                else:
                    down = False
                    cur -= 1
            else:
                if cur - 1 >= 0:
                    cur -= 1
                else:
                    down = True
                    cur += 1
        return ''.join(rows)
