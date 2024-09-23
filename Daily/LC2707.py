from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)
        minExtras = [0] * (n+1)
        for i in range(1, n+1):
            minExtras[i] = minExtras[i-1] + 1
            for j in range(i):
                if s[j:i] in wordSet and minExtras[j] < minExtras[i]:
                    minExtras[i] = minExtras[j]
        return minExtras[-1]
