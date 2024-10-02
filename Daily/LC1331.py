from bisect import bisect_right
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniqueSortedArr = sorted(set(arr))
        ranks = [bisect_right(uniqueSortedArr, x) for x in arr]
        return ranks
