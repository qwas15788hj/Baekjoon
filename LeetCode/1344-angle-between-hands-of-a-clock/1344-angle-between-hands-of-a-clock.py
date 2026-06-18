class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30 * hour + 0.5 * minutes
        m = 6 * minutes
        result = max(h, m) - min(h, m)
        return min(result, 360-result)