class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        i = 0
        keys = list(mapping.keys())
        result = ''
        while num > 0:
            while num - keys[i]  < 0:
                i += 1 
            result += mapping[keys[i]]
            num -= keys[i]
        return result
