from itertools import accumulate
from operator import xor
from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        accumulatedXor = list(accumulate(arr, xor, initial=0))
        results = [accumulatedXor[r+1] ^ accumulatedXor[l] for l, r in queries]
        return results
