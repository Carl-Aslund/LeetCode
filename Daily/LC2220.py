class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        difference = start ^ goal
        flipCount = 0
        while difference:
            flipCount += difference & 1
            difference >>= 1
        return flipCount
