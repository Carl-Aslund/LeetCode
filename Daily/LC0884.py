from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        totalCounts = Counter(s1.split()) + Counter(s2.split())
        return [word for word, count in totalCounts.items() if count == 1]
