class Solution:
    def numberToWords(self, num: int) -> str:
        lows = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',]
        highs = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']
        def parse(num, rank=0):
            res = []
            if num >= 1000:
                res = parse(num // 1000, rank+1)
            rem = num % 1000
            words = ''
            if rem // 100 > 0:
                words += lows[rem // 100] + ' Hundred'
                if rem % 100 > 0:
                    words += ' '
            if 0 < rem % 100 < 20:
                words += lows[rem % 100]
            else:
                words += highs[rem % 100 // 10] 
                if rem % 10 > 0:
                    words += ' ' + lows[rem % 10]
            if words != '':
                if rank > 0:
                    words += ' ' + thousands[rank]
                res.append(words)
            return res
        if num == 0:
            return lows[0]
        return ' '.join(parse(num))
