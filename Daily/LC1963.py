class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        for c in s:
            if c == '[':
                imbalance += 1
            elif imbalance:
                imbalance -= 1
        return (imbalance + 1)//2
