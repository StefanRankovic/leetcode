class Solution:
    def myAtoi(self, str: str) -> int:
        weight = 10
        result = 0
        sign = 1
        started = False
        for each in str:
            if each == ' ' and not started:
                continue
            if each == '-' and not started:
                sign = -1
                started = True
                continue
            if each == '+' and not started:
                sign = 1
                started = True
                continue
            if each.isdigit():
                started = True
                result *= weight
                result += int(each)
                if sign * result > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                if sign * result < - 2 ** 31:
                    return - 2 ** 31
            else:
                break
        return result * sign
            
