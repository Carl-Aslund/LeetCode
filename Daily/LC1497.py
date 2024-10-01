from collections import Counter
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = Counter(x % k for x in arr)
        return count[0] % 2 == 0 and all(count[i] == count[k - i] for i in range(1, k))
