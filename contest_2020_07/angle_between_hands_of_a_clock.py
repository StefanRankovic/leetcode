class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mdeg = minutes * 6
        hdeg = (hour * 30 + mdeg / 12) % 360
        diff = abs(hdeg - mdeg)
        return min(diff, 360 - diff)
